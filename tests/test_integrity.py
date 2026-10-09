"""Focused regressions for provenance and retained evidence; no live host evidence."""
import copy
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import evidence
import mini
import source_check


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')


class RepositoryIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'repo'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', 'build', '__pycache__'))

    def change_json(self, relative, mutate):
        path = self.root / relative
        value = mini.load(path)
        mutate(value)
        write_json(path, value)

    def test_license_is_in_public_payload_residue_scope(self):
        with (self.root / 'LICENSE').open('a') as stream:
            stream.write('\nlibfile_unit_test_identifier\n')
        with self.assertRaisesRegex(mini.Invalid, 'residue: LICENSE'):
            mini.validate_public_residue(self.root)

    def test_future_payload_member_is_automatically_scanned(self):
        from unittest.mock import patch
        (self.root / 'EXTRA.txt').write_text('libfile_unit_test_identifier')
        with patch.dict(mini.PAYLOAD, {'EXTRA.txt': 'EXTRA.txt'}):
            with self.assertRaisesRegex(mini.Invalid, 'residue: EXTRA.txt'):
                mini.validate_public_residue(self.root)

    def test_new_acceptance_docs_are_scanned(self):
        path = self.root / 'docs/new-acceptance-case.md'
        path.write_text('libfile_unit_test_identifier')
        with self.assertRaisesRegex(mini.Invalid, 'residue: docs/new-acceptance-case.md'):
            mini.validate_public_residue(self.root)

    def test_source_index_full_hash_drift_rejected(self):
        self.change_json('docs/source-index.json', lambda x: x.update(source_sha256='0' * 64))
        with self.assertRaisesRegex(mini.Invalid, 'provenance mismatch'):
            mini.validate_source_inventory(self.root)

    def test_source_map_component_hash_drift_rejected(self):
        self.change_json('docs/source-to-mini-map.json', lambda x: x['entries'][0].update(source_sha256='0' * 64))
        with self.assertRaisesRegex(mini.Invalid, 'component hash mismatch'):
            mini.validate_source_inventory(self.root)

    def test_source_map_rule_id_drift_rejected(self):
        self.change_json('docs/source-to-mini-map.json', lambda x: x['entries'][0]['source_rule_ids'].append('INVENTED'))
        with self.assertRaisesRegex(mini.Invalid, 'normative index mismatch'):
            mini.validate_source_inventory(self.root)

    def test_duplicate_index_pointer_rejected(self):
        self.change_json('docs/source-index.json', lambda x: x['pointers'].append(x['pointers'][0]))
        with self.assertRaisesRegex(mini.Invalid, 'pointer inventory'):
            mini.validate_source_inventory(self.root)

    def test_historical_and_current_scopes_pass_offline(self):
        self.assertFalse((self.root / '.git').exists())
        result = mini.validate_evidence_manifests(self.root)
        self.assertEqual(result['historical_entries'], 262)
        self.assertEqual(result['current_files'], 267)
        self.assertFalse(result['observations_authenticated'])

    def test_changed_current_readme_is_detected(self):
        path = self.root / 'release/4.0.0-candidate.5/README.md'
        path.write_bytes(path.read_bytes() + b'\nunreviewed change\n')
        with self.assertRaisesRegex(mini.Invalid, 'integrity mismatch: release/4.0.0-candidate.5/README.md'):
            mini.validate_evidence_manifests(self.root)

    def test_changed_preserved_readme_is_detected(self):
        path = self.root / 'docs/integrity/candidate-5-original-README.md'
        path.write_bytes(path.read_bytes() + b'\nchanged history\n')
        with self.assertRaisesRegex(mini.Invalid, 'EVIDENCE_MANIFEST.json:README.md'):
            mini.validate_evidence_manifests(self.root)

    def test_old_manifest_cannot_be_silently_regenerated(self):
        path = self.root / 'release/4.0.0-candidate.5/EVIDENCE_MANIFEST.json'
        path.write_bytes(path.read_bytes() + b'\n')
        with self.assertRaisesRegex(mini.Invalid, 'Historical manifest changed'):
            mini.validate_evidence_manifests(self.root)

    def test_new_unlisted_evidence_is_detected(self):
        (self.root / 'release/4.0.0-candidate.5/unreviewed.txt').write_text('new')
        with self.assertRaisesRegex(mini.Invalid, 'file inventory mismatch'):
            mini.validate_evidence_manifests(self.root)

    def test_missing_current_only_publication_file_is_detected(self):
        (self.root / 'release/4.0.0-candidate.5/PUBLICATION_STATUS.md').unlink()
        with self.assertRaisesRegex(mini.Invalid, 'file inventory mismatch'):
            mini.validate_evidence_manifests(self.root)

    def test_preserved_path_cannot_escape_repository(self):
        def escape(policy):
            policy['historical_manifests'][1]['preserved_entries']['README.md']['path'] = '../outside.md'
        self.change_json('docs/integrity/evidence-manifests.json', escape)
        with self.assertRaisesRegex(mini.Invalid, 'Unsafe manifest path'):
            mini.validate_evidence_manifests(self.root)


class ExactSourceCheckTests(unittest.TestCase):
    """Synthetic complete source fixture: never contains the user's private master."""
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        identity = {name: {'id': 'fixture.' + name, 'version': '1.0.0'}
                    for name in ('runtime', 'schema', 'system_contract')}
        self.master = {'identity': identity,
                       'bootstrap': {'id': 'FIXTURE.BOOT', 'instruction': 'Synthetic source fixture only.'},
                       'procedures': {'turn': {'id': 'FIXTURE.TURN', 'instruction': 'Not live behavior.'}},
                       'core': {'truth': {'id': 'FIXTURE.TRUTH', 'statement': 'Synthetic normative statement.'}},
                       'owners': {}, 'routing': {}}
        self.path = self.root / 'synthetic-master.json'
        write_json(self.path, self.master)
        pointers = ['#/identity/runtime', '#/identity/schema', '#/identity/system_contract', '#/bootstrap',
                    '#/procedures/turn', '#/core/truth', '#/owners', '#/routing']
        entries = [{'source_pointer': pointer, 'source_sha256': mini.sha(mini.canonical(mini.resolve(self.master, pointer))),
                    'source_rule_ids': source_check.atomic_ids(mini.resolve(self.master, pointer))} for pointer in pointers]
        digest = mini.sha(self.path.read_bytes())
        self.mapping = {'source_sha256': digest, 'inventory_complete': True, 'entries': entries}
        self.index = {'source_sha256': digest, 'pointers': pointers,
                      'normative_ids': [i for row in entries for i in row['source_rule_ids']],
                      'component_sha256': {row['source_pointer']: row['source_sha256'] for row in entries}}
        self.provenance = {'source': {**copy.deepcopy(identity), 'sha256': digest}}
        self.save_records()

    def save_records(self):
        for name, value in [('source-index', self.index), ('source-to-mini-map', self.mapping), ('source-manifest', self.provenance)]:
            write_json(self.root / ('docs/' + name + '.json'), value)

    def test_exact_synthetic_source_passes_with_bounded_claim(self):
        result = source_check.verify_source(self.path, self.root)
        self.assertEqual(result['components'], 8)
        self.assertEqual(result['normative_ids'], 3)
        self.assertEqual(result['semantic_equivalence'], 'not_asserted')

    def test_changed_raw_bytes_rejected_even_if_json_unchanged(self):
        self.path.write_bytes(self.path.read_bytes().replace(b'\n', b'\r\n'))
        with self.assertRaisesRegex(mini.Invalid, 'Wrong full source hash'):
            source_check.verify_source(self.path, self.root)

    def test_identity_mismatch_rejected(self):
        self.provenance['source']['runtime']['version'] = '2.0.0'
        self.save_records()
        with self.assertRaisesRegex(mini.Invalid, 'identity mismatch: runtime'):
            source_check.verify_source(self.path, self.root)

    def test_consistently_forged_component_hash_rejected_against_actual_source(self):
        self.mapping['entries'][0]['source_sha256'] = '0' * 64
        self.index['component_sha256']['#/identity/runtime'] = '0' * 64
        self.save_records()
        mini.validate_source_inventory(self.root)  # Cross-file agreement alone is not source verification.
        with self.assertRaisesRegex(mini.Invalid, 'Source component changed'):
            source_check.verify_source(self.path, self.root)

    def test_consistently_forged_normative_id_rejected(self):
        self.mapping['entries'][3]['source_rule_ids'] = ['FORGED']
        self.index['normative_ids'][0] = 'FORGED'
        self.save_records()
        with self.assertRaisesRegex(mini.Invalid, 'Normative ID inventory mismatch'):
            source_check.verify_source(self.path, self.root)

    def test_consistently_missing_component_rejected(self):
        removed = self.mapping['entries'].pop()
        self.index['pointers'].pop()
        del self.index['component_sha256'][removed['source_pointer']]
        self.save_records()
        with self.assertRaisesRegex(mini.Invalid, 'Source component inventory/order differs'):
            source_check.verify_source(self.path, self.root)


class NegativeSourceHashTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        text = 'SYNTHETIC TEST ONLY: no actual source or host observation.'
        (self.base / 'transcript.txt').write_text(text)
        self.observation = {'availability': 'mismatch', 'runtime_body_observed': False,
                            'system_body_observed': False, 'runtime_sha256': '0' * 64, 'system_sha256': None,
                            'evidence': {'path': 'transcript.txt', 'sha256': mini.sha(text.encode()), 'excerpt': text}}

    def test_well_formed_different_hash_can_record_mismatch(self):
        evidence.check_source_observation(self.observation, self.base)

    def test_malformed_hashes_rejected_in_negative_observations(self):
        for key in ['runtime_sha256', 'system_sha256']:
            for value in [[], 123, False, {}, '', 'bad', 'A' * 64]:
                observed = copy.deepcopy(self.observation)
                observed[key] = value
                with self.subTest(key=key, value=value), self.assertRaisesRegex(mini.Invalid, 'Source hash must'):
                    evidence.check_source_observation(observed, self.base)

    def test_mismatch_requires_observed_hash_value(self):
        self.observation['runtime_sha256'] = None
        with self.assertRaisesRegex(mini.Invalid, 'different valid runtime hash'):
            evidence.check_source_observation(self.observation, self.base)

    def test_observed_system_body_needs_hash(self):
        self.observation['system_body_observed'] = True
        with self.assertRaisesRegex(mini.Invalid, 'Observed complete body requires source hash: system'):
            evidence.check_source_observation(self.observation, self.base)


if __name__ == '__main__':
    unittest.main()
