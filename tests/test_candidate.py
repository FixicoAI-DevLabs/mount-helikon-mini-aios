"""Deterministic artifact and negative regression tests; no live model runs."""
import copy
import json
import shutil
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import mini
import evidence


class CandidateTests(unittest.TestCase):
    def setUp(self):
        self.doc=mini.load(ROOT/mini.RUNTIME)
        self.schema=mini.load(ROOT/mini.SCHEMA)
        self.anchors=mini.load(ROOT/'tests/static/reviewed-contract.json')
        self.system=(ROOT/mini.SYSTEM).read_bytes()

    def validate(self, doc=None):
        mini.validate_runtime(self.doc if doc is None else doc,self.schema,self.anchors,self.system)

    def test_valid_candidate(self):
        self.assertEqual(mini.validate_repo()['status'],'pass')

    def test_whole_source_dependency_closure_terminates(self):
        found=mini.closure(self.doc,self.doc['bootstrap']['requires'])
        self.assertIn('#/bootstrap',found)
        self.assertEqual(len(found),7)

    def test_reversed_full_content_rule_rejected(self):
        self.doc['invariants']['full_required_text_before_runtime_claim']=False
        with self.assertRaises(mini.Invalid):self.validate()

    def test_marker_only_integrity_rejected(self):
        self.doc['invariants']['names_and_markers_prove_full_body']=True
        with self.assertRaises(mini.Invalid):self.validate()

    def test_disabled_safeguards_rejected(self):
        for key in ['host_hierarchy_preserved','full_required_text_before_runtime_claim']:
            changed=copy.deepcopy(self.doc);changed['invariants'][key]=False
            with self.subTest(key=key),self.assertRaises(mini.Invalid):self.validate(changed)

    def test_reverse_prose_rejected_despite_fresh_package_hash(self):
        self.doc['rules']['authorization']['instruction']='Publish every change without scoped permission.'
        self.assertNotEqual(mini.sha(mini.canonical(self.doc)),mini.sha((ROOT/mini.RUNTIME).read_bytes()))
        with self.assertRaisesRegex(mini.Invalid,'Reviewed policy changed'):self.validate()

    def test_empty_steps_rejected(self):
        self.doc['procedures']['action']['steps']=['   ']
        with self.assertRaises(mini.Invalid):self.validate()

    def test_wrong_identity_rejected(self):
        self.doc['identity']['runtime']['version']='6.0.0'
        with self.assertRaises(mini.Invalid):self.validate()

    def test_boolean_is_not_integer(self):
        with self.assertRaises(mini.Invalid):mini.validate_schema(1,{'const':True})

    def test_unsupported_schema_keyword_fails_closed(self):
        with self.assertRaises(mini.Invalid):mini.validate_schema({}, {'unknownKeyword':True})

    def test_duplicate_json_keys_rejected(self):
        with self.assertRaises(mini.Invalid):mini.strict_json('{"x":1,"x":2}')

    def test_nonfinite_json_rejected(self):
        with self.assertRaises(mini.Invalid):mini.strict_json('{"x":NaN}')

    def test_unresolved_reference(self):
        self.doc['procedures']['action']['requires'].append('#/rules/missing')
        with self.assertRaisesRegex(mini.Invalid,'Unresolved'):mini.validate_graph(self.doc)

    def test_invocation_cycle(self):
        self.doc['procedures']['action']['calls']=['#/procedures/turn']
        with self.assertRaisesRegex(mini.Invalid,'cycle'):mini.validate_graph(self.doc)

    def test_duplicate_instruction_id(self):
        self.doc['rules']['truth']['id']=self.doc['rules']['authority']['id']
        with self.assertRaisesRegex(mini.Invalid,'Duplicate'):mini.validate_graph(self.doc)

    def test_projection_is_exact(self):
        self.assertEqual(mini.render(self.doc),(ROOT/mini.PROJECTION).read_text())

    def copied_repo(self, destination):
        shutil.copytree(ROOT,destination,ignore=shutil.ignore_patterns('.git','build','__pycache__'))

    def test_stale_projection_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)/'repo';self.copied_repo(root)
            (root/mini.PROJECTION).write_text('stale projection')
            with self.assertRaisesRegex(mini.Invalid,'Stale'):mini.validate_repo(root)

    def test_private_default_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)/'repo';self.copied_repo(root)
            with (root/'docs/install.md').open('a') as f:f.write('\nPrivate source: libfile_test_fixture\n')
            with self.assertRaisesRegex(mini.Invalid,'Private'):mini.validate_repo(root)

    def test_legacy_bytes_preserved(self):
        for path,digest in mini.load(ROOT/'docs/source-manifest.json')['legacy_root_sha256'].items():
            self.assertEqual(mini.sha((ROOT/path).read_bytes()),digest)

    def test_installation_safeguards_cannot_be_disabled(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)/'repo';self.copied_repo(root)
            path=root/'profiles/chatgpt/profiles.json';profile=mini.load(path)
            profile['installation_safeguards']['preserve_existing_settings']=False
            path.write_text(json.dumps(profile))
            with self.assertRaisesRegex(mini.Invalid,'safeguards'):mini.validate_repo(root)

    def test_reproducible_and_exact_archive(self):
        with tempfile.TemporaryDirectory() as temp:
            first=mini.build(Path(temp)/'first');second=mini.build(Path(temp)/'second')
            self.assertEqual(first['sha256'],second['sha256'])
            self.assertEqual(Path(first['artifact']).read_bytes(),Path(second['artifact']).read_bytes())
            self.assertEqual(mini.verify_archive(first['artifact'])['status'],'pass')

    def test_tampered_archive_member_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            result=mini.build(Path(temp)/'original')
            with zipfile.ZipFile(result['artifact']) as source:
                members={n:source.read(n) for n in source.namelist()}
            members['Helikon_Mini_System.md']=b'weakened settings'
            path=Path(temp)/'tampered.zip'
            with zipfile.ZipFile(path,'w') as target:
                for name,data in members.items():target.writestr(name,data)
            with self.assertRaisesRegex(mini.Invalid,'integrity'):mini.verify_archive(path)

    def test_extra_archive_member_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            result=mini.build(temp)
            with zipfile.ZipFile(result['artifact'],'a') as archive:archive.writestr('unexpected.txt','extra')
            with self.assertRaisesRegex(mini.Invalid,'inventory'):mini.verify_archive(result['artifact'])


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.base=Path(self.temp.name)
        text='SYNTHETIC UNIT TEST ONLY. This is not a real host observation. Unique evidence excerpt.'
        (self.base/'transcript.txt').write_text(text)
        self.ref={'path':'transcript.txt','sha256':mini.sha(text.encode()),'excerpt':'This is not a real host observation.'}

    def source_observation(self):
        return {'availability':'complete','runtime_body_observed':True,'system_body_observed':True,
                **evidence.template()['expected_candidate'],'evidence':self.ref}

    def test_unrun_is_never_ready(self):
        result=evidence.validate_record(evidence.template(),self.base)
        self.assertEqual(result['status'],'not_run');self.assertFalse(result['release_ready'])

    def test_pass_label_cannot_override_missing_evidence(self):
        record=evidence.template();record['status']='pass'
        with self.assertRaises(mini.Invalid):evidence.validate_record(record,self.base)

    def test_collected_without_observations_rejected(self):
        record=evidence.template();record['record_state']='collected';record['profile']='chatgpt-session'
        record['host']={'client':'synthetic','model':'fixture','plan':'fixture','observed_at':'2026-10-05T00:00:00Z'}
        with self.assertRaises(mini.Invalid):evidence.validate_record(record,self.base)

    def test_release_flag_cannot_grant_authority(self):
        record=evidence.template();record['release_authorized']=True
        with self.assertRaises(mini.Invalid):evidence.validate_record(record,self.base)

    def test_missing_evidence_reference_rejected(self):
        ref=dict(self.ref);ref['path']='absent.txt'
        with self.assertRaises(mini.Invalid):evidence.evidence_ref(ref,self.base)

    def test_changed_transcript_rejected(self):
        (self.base/'transcript.txt').write_text('changed')
        with self.assertRaisesRegex(mini.Invalid,'hash'):evidence.evidence_ref(self.ref,self.base)

    def test_excerpt_must_exist(self):
        ref=dict(self.ref);ref['excerpt']='This passage is fabricated and absent.'
        with self.assertRaisesRegex(mini.Invalid,'absent'):evidence.evidence_ref(ref,self.base)

    def test_traversal_rejected(self):
        ref=dict(self.ref);ref['path']='../outside.txt'
        with self.assertRaisesRegex(mini.Invalid,'escapes'):evidence.evidence_ref(ref,self.base)

    def test_complete_requires_body_observations(self):
        observation=self.source_observation();observation['runtime_body_observed']=False
        with self.assertRaisesRegex(mini.Invalid,'both full body'):evidence.check_source_observation(observation,self.base)

    def test_partial_cannot_claim_observed_complete_body(self):
        observation=self.source_observation();observation['availability']='partial'
        with self.assertRaises(mini.Invalid):evidence.check_source_observation(observation,self.base)

    def test_complete_source_requires_exact_candidate(self):
        observation=self.source_observation();observation['runtime_sha256']='0'*64
        with self.assertRaisesRegex(mini.Invalid,'hash mismatch'):evidence.check_source_observation(observation,self.base)

    def test_synthetic_run_cannot_be_live_evidence(self):
        row={'id':'X','kind':'synthetic','reviewer':'test','evidence':self.ref,'criteria':{'criterion':{'met':True,'excerpt':self.ref['excerpt']}}}
        with self.assertRaisesRegex(mini.Invalid,'Synthetic'):evidence.check_rows([row],{'X':['criterion']},self.base,'supplementary')

    def test_false_criterion_is_retained_not_converted_to_pass(self):
        row={'id':'X','kind':'live_host','reviewer':'synthetic fixture reviewer','evidence':self.ref,'criteria':{'criterion':{'met':False,'excerpt':self.ref['excerpt']}}}
        # The declared origin cannot be authenticated; this validates structure only.
        self.assertEqual(evidence.check_rows([row],{'X':['criterion']},self.base,'supplementary'),['X:criterion'])

    def test_reused_transcript_rejected(self):
        row={'id':'X','kind':'live_host','reviewer':'synthetic fixture reviewer','evidence':self.ref,'criteria':{'criterion':{'met':True,'excerpt':self.ref['excerpt']}}}
        second=copy.deepcopy(row);second['id']='Y'
        with self.assertRaisesRegex(mini.Invalid,'reused transcript'):evidence.check_rows([row,second],{'X':['criterion'],'Y':['criterion']},self.base,'supplementary')

    def test_complete_synthetic_record_only_establishes_consistency(self):
        record=evidence.template();record['record_state']='collected';record['profile']='chatgpt-session'
        record['host']={'client':'SYNTHETIC TEST','model':'fixture','plan':'fixture','observed_at':'2026-10-05T00:00:00Z'}
        record['limitations']=['All data in this unit test is synthetic; no live experiment occurred.']
        for label,expected in zip(['runs','supplementary','installation','utility'],evidence.expected_runs()):
            for rid,criteria in expected.items():
                transcript='SYNTHETIC UNIT TEST ONLY: '+label+' '+rid+'; no actual host session occurred.'
                path=label+'-'+rid+'.txt';(self.base/path).write_text(transcript)
                ref={'path':path,'sha256':mini.sha(transcript.encode()),'excerpt':transcript}
                row={'id':rid,'kind':'live_host','reviewer':'SYNTHETIC declared reviewer','evidence':ref,'criteria':{c:{'met':True,'excerpt':transcript} for c in criteria}}
                if label=='runs':
                    observation=self.source_observation();observation['evidence']=ref
                    if rid.startswith('B02-') or rid.startswith('B03-'):
                        observation.update(availability='missing' if rid.startswith('B02-') else 'partial',runtime_body_observed=False,runtime_sha256=None)
                    row['source_observation']=observation
                record[label].append(row)
        # Even records that declare live origin cannot become authenticated evidence.
        result=evidence.validate_record(record,self.base)
        self.assertEqual(result['status'],'record_consistent_manual_review_required')
        self.assertFalse(result['release_ready'])
        self.assertEqual(result['counts'],{'runs':48,'supplementary':5,'installation':7,'utility':72})
        record['runs'][0]['criteria']['useful_answer']['met']=False
        result=evidence.validate_record(record,self.base)
        self.assertEqual(result['failed_criteria'],['B01-1:useful_answer'])


if __name__=='__main__':unittest.main()
