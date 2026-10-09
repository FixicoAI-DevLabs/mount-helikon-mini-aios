"""Protect the restored account installation contract and reject false evidence scopes."""
import copy
import contextlib
import io
import json
import shutil
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import installer
import mini


class InstallerArtifactTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        shutil.copytree(ROOT/'installer',self.root/'installer')
        shutil.copy(ROOT/installer.RUNTIME,self.root/installer.RUNTIME)
        for name in ('START_HERE.md','Helikon_Mini_QA.md'):
            shutil.copy(ROOT/name,self.root/name)
        installer.render(self.root)

    def change_contract(self, edit):
        path=self.root/'installer/contract.json';doc=json.loads(path.read_text());edit(doc)
        path.write_text(json.dumps(doc));installer.render(self.root)

    def test_stale_embedded_runtime_is_rejected(self):
        path=self.root/installer.PACKAGE;p=json.loads(path.read_text())
        p['operating_layer']['exact_runtime_text']='{}';path.write_text(json.dumps(p))
        with self.assertRaisesRegex(ValueError,'Stale'):installer.validate(self.root)

    def test_copy_sheet_cannot_drift(self):
        (self.root/'Helikon_Mini_System.md').write_text('old project instructions')
        with self.assertRaisesRegex(ValueError,'projection'):installer.validate(self.root)

    def test_copy_sheet_fences_do_not_add_newlines_to_canonical_snippets(self):
        for relative in (installer.SYSTEM, installer.PROFILE):
            path=self.root/relative
            path.write_bytes(path.read_bytes().rstrip(b'\n'))
        p=installer.render(self.root)
        sheet=(self.root/'Helikon_Mini_System.md').read_text()
        for key, snippet in p['system_layer']['exact_install_text'].items():
            with self.subTest(key=key):
                self.assertFalse(snippet.endswith('\n'))
                self.assertIn('```text\n'+snippet+'\n```\n',sheet)
                self.assertEqual(p['system_layer']['payload_sha256'][key],installer.sha(snippet.encode()))
        self.assertEqual(installer.validate(self.root)['status'],'pass')

    def test_record_check_rejects_package_and_projection_drift(self):
        record=installer.record_template(self.root)
        path=self.root/installer.PACKAGE
        p=json.loads(path.read_text())
        p['system_layer']['exact_install_text']['custom_instructions']='different packaged snippet'
        path.write_text(json.dumps(p))
        with self.assertRaisesRegex(ValueError,'Stale or modified'):
            installer.verify_record(record,self.root,self.root)
        installer.render(self.root)
        (self.root/installer.SYSTEM).write_text('different source snippet')
        with self.assertRaisesRegex(ValueError,'Stale or modified'):
            installer.verify_record(record,self.root,self.root)

    def test_runtime_line_ending_change_is_not_hidden(self):
        path=self.root/installer.RUNTIME
        path.write_bytes(path.read_bytes().replace(b'\n',b'\r\n'))
        with self.assertRaisesRegex(ValueError,'Stale'):installer.validate(self.root)

    def test_regenerated_crlf_runtime_preserves_exact_bytes_and_hash(self):
        path=self.root/installer.RUNTIME
        previous_hash=installer.sha(path.read_bytes())
        raw=path.read_bytes().replace(b'\n',b'\r\n');path.write_bytes(raw)
        p=installer.render(self.root)
        self.assertEqual(p['operating_layer']['exact_runtime_text'].encode('utf-8'),raw)
        self.assertEqual(p['operating_layer']['sha256'],installer.sha(raw))
        with self.assertRaisesRegex(ValueError,'Profile SHA-256 binding'):installer.validate(self.root)
        profile=self.root/installer.PROFILE
        profile.write_text(profile.read_text().replace(previous_hash,installer.sha(raw)))
        installer.render(self.root)
        self.assertEqual(installer.validate(self.root)['status'],'pass')

    def test_profile_hash_cannot_disagree_after_regeneration(self):
        path=self.root/installer.PROFILE
        actual_hash=installer.package(self.root)['operating_layer']['sha256']
        path.write_text(path.read_text().replace(actual_hash,'0'*64));installer.render(self.root)
        with self.assertRaisesRegex(ValueError,'Profile SHA-256 binding'):installer.validate(self.root)

    def test_each_profile_identity_pair_must_match_runtime(self):
        path=self.root/installer.PROFILE;original=path.read_text()
        for label in ('Runtime','Schema','System contract','Extension contract'):
            with self.subTest(label=label):
                lines=original.splitlines()
                lines=[label+': stale.identity@0.0.0.' if line.startswith(label+':') else line for line in lines]
                path.write_text('\n'.join(lines)+'\n');installer.render(self.root)
                with self.assertRaisesRegex(ValueError,'Profile '+label+' binding'):installer.validate(self.root)

    def test_duplicate_profile_bindings_cannot_hide_a_conflict(self):
        path=self.root/installer.PROFILE
        text=path.read_text().replace('[HELIKON_MINI_PROFILE_END]',
                                      'Runtime: stale@0.0.0.\n[HELIKON_MINI_PROFILE_END]')
        path.write_text(text);installer.render(self.root)
        with self.assertRaisesRegex(ValueError,'Profile Runtime binding'):installer.validate(self.root)

    def test_projection_line_ending_change_is_detected(self):
        path=self.root/'Helikon_Mini_System.md'
        path.write_bytes(path.read_bytes().replace(b'\n',b'\r\n'))
        with self.assertRaisesRegex(ValueError,'projection'):installer.validate(self.root)

    def test_oversize_snippet_rejected_even_after_regeneration(self):
        (self.root/installer.SYSTEM).write_text('x'*1501);installer.render(self.root)
        with self.assertRaisesRegex(ValueError,'bounded'):installer.validate(self.root)

    def test_project_requirement_cannot_return(self):
        self.change_contract(lambda d:d.update(projects_required=True))
        with self.assertRaisesRegex(ValueError,'Project-only'):installer.validate(self.root)

    def test_memory_runtime_cannot_return(self):
        self.change_contract(lambda d:d['source'].update(memory_writes_required=True))
        with self.assertRaisesRegex(ValueError,'memory'):installer.validate(self.root)

    def test_full_helikon_protection_required(self):
        self.change_contract(lambda d:d.update(protect_active_full_helikon=False))
        with self.assertRaisesRegex(ValueError,'protection'):installer.validate(self.root)

    def test_handoff_projection_cannot_drift(self):
        path=self.root/'START_HERE.md'
        path.write_text(path.read_text().replace('Check my installed Helikon Mini source access','Claim Mini is ready'))
        with self.assertRaisesRegex(ValueError,'handoff projection'):installer.validate(self.root)

    def test_bare_command_cannot_replace_handoff_block(self):
        path=self.root/'Helikon_Mini_QA.md';path.write_text('FINAL_VERIFY')
        with self.assertRaisesRegex(ValueError,'marker inventory'):installer.validate(self.root)

    def test_handoff_cannot_allow_attachments(self):
        self.change_contract(lambda d:d['fresh_chat_handoff'].update(attachments_allowed=True))
        with self.assertRaisesRegex(ValueError,'without attachments'):installer.validate(self.root)

    def test_smaller_snippet_design_budget_is_enforced(self):
        self.change_contract(lambda d:d['personalization_contract']['snippet_design_budgets'].update(custom_instructions=1))
        with self.assertRaisesRegex(ValueError,'design budget'):installer.validate(self.root)

    def test_bundle_has_eight_end_user_files(self):
        self.assertEqual(len(mini.PAYLOAD)+1,8)
        self.assertIn(installer.PACKAGE.name,mini.PAYLOAD)
        self.assertFalse(any(p.startswith(('tools/','tests/','schema/')) for p in mini.PAYLOAD.values()))


class InstallationEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.base=Path(self.temp.name)
        self.ref=self.save('transcript.txt','SYNTHETIC UNIT FIXTURE. Not a live host test.')
        self.runtime_ref=self.save('runtime.json',(ROOT/installer.RUNTIME).read_text())

    def save(self,name,text):
        (self.base/name).write_text(text)
        return {'path':name,'sha256':installer.sha(text.encode()),'excerpt':text[:30]}

    def observation(self,surface):
        return {'source_ref':'synthetic-unit-fixture-source','full_runtime_file':self.runtime_ref,
                'evidence':self.ref,'surface':surface,'source_method':'supported_file_read',
                'observation_method':'direct_observation'}

    def complete_synthetic_record(self):
        record=installer.record_template();record['surface']='ordinary_non_project_chat'
        texts=installer.package()['system_layer']['exact_install_text']
        record['settings_readback']={**texts,'evidence':self.save('settings.txt','\n'.join(texts.values())),
                                     'unrelated_content_preserved':True,'observation_method':'direct_observation'}
        record['runtime_readback']=self.observation('account_library')
        record['ordinary_chat_readback']=self.observation('fresh_ordinary_non_project_chat_without_attachment')
        record['behavior_results']=[{'id':i,'status':'passed','observation_method':'direct_observation','evidence':self.ref} for i in
                                    ['exact_json','duration_capacity','missing_source','wrong_source']]
        record['host']={'client':'Synthetic client','plan':'Synthetic plan','model':'Synthetic model',
                        'observed_at':'2026-10-07T14:00:00-06:00',
                        'observation_method':'direct_observation','evidence':self.ref}
        record['backup']={'status':'passed','observation_method':'direct_observation',
                          'exact_backup_exists':True,'storage_description':'Synthetic fixture only','evidence':self.ref}
        for row in record['checkpoints'].values():
            row.update(status='passed',observation_method='direct_observation',evidence=[self.ref])
        record['limitations']=['Synthetic fixture, never release evidence.']
        return record

    def test_empty_template_is_incomplete(self):
        result=installer.verify_record(installer.record_template(),self.base)
        self.assertEqual(result['status'],'incomplete');self.assertFalse(result['release_ready'])

    def test_consistency_cannot_certify_a_host(self):
        result=installer.verify_record(self.complete_synthetic_record(),self.base)
        self.assertEqual(result['status'],'record_consistent_manual_review_required')
        self.assertFalse(result['release_ready'])

    def test_project_work_and_attachment_do_not_pass_ordinary_access(self):
        for surface in ['chatgpt-project','work','fresh_ordinary_chat_with_attachment']:
            with self.subTest(surface=surface):
                record=self.complete_synthetic_record();record['ordinary_chat_readback']['surface']=surface
                with self.assertRaisesRegex(ValueError,'cannot establish'):installer.verify_record(record,self.base)

    def test_download_does_not_prove_library_storage(self):
        record=self.complete_synthetic_record();record['runtime_readback']['surface']='local_download'
        with self.assertRaisesRegex(ValueError,'account Library'):installer.verify_record(record,self.base)

    def test_wrong_runtime_content_rejected(self):
        record=self.complete_synthetic_record()
        record['ordinary_chat_readback']['full_runtime_file']=self.save('wrong.json','{"identity":"wrong"}')
        with self.assertRaisesRegex(ValueError,'differs'):installer.verify_record(record,self.base)

    def test_both_settings_must_be_present(self):
        record=self.complete_synthetic_record();record['settings_readback']['more_about_you']='personal details only'
        with self.assertRaisesRegex(ValueError,'omit'):installer.verify_record(record,self.base)

    def test_saved_snippets_can_preserve_unrelated_text_and_source_binding(self):
        record=self.complete_synthetic_record()
        for key in ('custom_instructions','more_about_you'):
            record['settings_readback'][key]=('Existing preference.\n'+record['settings_readback'][key]
                                               +'\nLater unrelated preference.\n')
        record['settings_readback']['more_about_you']+='Mini source binding: synthetic-unit-fixture-source'
        result=installer.verify_record(record,self.base)
        self.assertEqual(result['status'],'record_consistent_manual_review_required')

    def test_invented_pass_flag_rejected(self):
        record=installer.record_template();record['release_ready']=True
        with self.assertRaisesRegex(ValueError,'fields differ'):installer.verify_record(record,self.base)

    def test_failed_behavior_remains_incomplete(self):
        record=self.complete_synthetic_record();record['behavior_results'][0]['status']='failed'
        result=installer.verify_record(record,self.base)
        self.assertEqual(result['status'],'incomplete');self.assertIn('failed:exact_json',result['missing_or_failed'])

    def test_changed_evidence_rejected(self):
        record=self.complete_synthetic_record();(self.base/'transcript.txt').write_text('changed')
        with self.assertRaisesRegex(ValueError,'mismatch'):installer.verify_record(record,self.base)

    def test_template_covers_every_checkpoint_and_behavior_with_not_run(self):
        record=installer.record_template()
        self.assertEqual(set(record['checkpoints']),set(installer.package()['installer']['checkpoints']))
        self.assertEqual(len(record['checkpoints']),8)
        self.assertTrue(all(row['status']=='not_run' for row in record['checkpoints'].values()))
        self.assertTrue(all(row['status']=='not_run' for row in record['behavior_results']))

    def test_failed_and_unknown_checkpoint_cannot_complete(self):
        for state in ('failed','unknown','not_run'):
            with self.subTest(state=state):
                record=self.complete_synthetic_record()
                record['checkpoints']['exact_package_read']['status']=state
                result=installer.verify_record(record,self.base)
                self.assertEqual(result['status'],'incomplete')
                self.assertIn(state+':exact_package_read',result['missing_or_failed'])

    def test_missing_checkpoint_and_behavior_rows_rejected(self):
        record=self.complete_synthetic_record();del record['checkpoints']['exact_package_read']
        with self.assertRaisesRegex(ValueError,'inventory'):installer.verify_record(record,self.base)
        record=self.complete_synthetic_record();record['behavior_results'].pop()
        with self.assertRaisesRegex(ValueError,'inventory'):installer.verify_record(record,self.base)

    def test_complete_record_requires_host_metadata_and_observation_method(self):
        record=self.complete_synthetic_record();record['host']['plan']=None
        result=installer.verify_record(record,self.base)
        self.assertEqual(result['status'],'incomplete');self.assertIn('host:plan',result['missing_or_failed'])
        record=self.complete_synthetic_record();record['settings_readback']['observation_method']='not_recorded'
        with self.assertRaisesRegex(ValueError,'observation method'):installer.verify_record(record,self.base)

    def test_host_date_requires_timezone(self):
        record=self.complete_synthetic_record();record['host']['observed_at']='2026-10-07T14:00:00'
        with self.assertRaisesRegex(ValueError,'timezone'):installer.verify_record(record,self.base)

    def test_user_reported_observations_remain_distinguishable(self):
        record=self.complete_synthetic_record();record['host']['observation_method']='user_reported'
        result=installer.verify_record(record,self.base)
        self.assertEqual(result['user_reported_observations'],['host_metadata'])
        self.assertFalse(result['release_ready'])

    def test_backup_claim_requires_existence_and_evidence(self):
        record=self.complete_synthetic_record();record['backup']['exact_backup_exists']=False
        with self.assertRaisesRegex(ValueError,'exact stored backup'):installer.verify_record(record,self.base)
        record=self.complete_synthetic_record();record['backup']['evidence']=None
        with self.assertRaisesRegex(ValueError,'backup needs evidence'):installer.verify_record(record,self.base)

    def test_passed_checkpoint_cannot_omit_evidence(self):
        record=self.complete_synthetic_record();record['checkpoints']['exact_package_read']['evidence']=[]
        with self.assertRaisesRegex(ValueError,'checkpoint needs evidence'):installer.verify_record(record,self.base)

    def test_evidence_cannot_escape_record_directory(self):
        record=self.complete_synthetic_record()
        record['host']['evidence']={**self.ref,'path':'../outside.txt'}
        with self.assertRaisesRegex(ValueError,'escapes'):installer.verify_record(record,self.base)

    def test_malformed_status_rejected_cleanly(self):
        record=self.complete_synthetic_record();record['backup']['status']={}
        with self.assertRaisesRegex(ValueError,'invalid status'):installer.verify_record(record,self.base)

    def test_legacy_record_cannot_satisfy_current_acceptance(self):
        record=self.complete_synthetic_record()
        for key in ('host','checkpoints','backup','installer_protocol_version'):del record[key]
        record['record_version']='1.0.0'
        for key in ('settings_readback','runtime_readback','ordinary_chat_readback'):
            del record[key]['observation_method']
        record['behavior_results']=[{'id':row['id'],'passed':True,'evidence':row['evidence']}
                                    for row in record['behavior_results']]
        result=installer.verify_record(record,self.base)
        self.assertEqual(result['status'],'legacy_record_manual_review_required')
        self.assertFalse(result['release_ready'])
        record['package_version']='historical-version'
        self.assertEqual(installer.verify_record(record,self.base)['status'],
                         'legacy_record_requires_matching_package')

    def test_protocol_mismatch_is_rejected(self):
        record=self.complete_synthetic_record();record['installer_protocol_version']='0.0.0'
        with self.assertRaisesRegex(ValueError,'protocol'):installer.verify_record(record,self.base)

    def test_record_template_cli_preserves_existing_file(self):
        path=self.base/'record.json';path.write_text('existing private evidence')
        with contextlib.redirect_stdout(io.StringIO()):
            code=installer.main(['record-template','--out',str(path)])
        self.assertEqual(code,1);self.assertEqual(path.read_text(),'existing private evidence')

    def test_verify_cli_distinguishes_incomplete_consistent_and_invalid(self):
        path=self.base/'record.json'
        for record, expected in ((installer.record_template(),2),
                                 (self.complete_synthetic_record(),0),
                                 ({'record_version':'invalid'},1)):
            with self.subTest(expected=expected):
                path.write_text(json.dumps(record))
                with contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(installer.main(['verify-record',str(path)]),expected)


class ExactSnippetReadbackTests(unittest.TestCase):
    """Exercise persisted-text comparisons independently of changing releases."""

    def readback(self,p,texts,legacy=False):
        record={'surface':'ordinary_non_project_chat',
                'settings_readback':{**texts,'evidence':{},'unrelated_content_preserved':True},
                'runtime_readback':None,'ordinary_chat_readback':None}
        if not legacy:record['settings_readback']['observation_method']='direct_observation'
        return installer._readbacks(record,p,lambda ref:None,legacy=legacy)

    def test_historical_package_terminal_newline_is_still_required(self):
        path=ROOT/'release/4.1.1-candidate.1/Helikon-Mini-4.1.1-candidate.1.zip'
        with zipfile.ZipFile(path) as archive:
            p=json.loads(archive.read(installer.PACKAGE.name))
        canonical=p['system_layer']['exact_install_text']
        for legacy in (False,True):
            with self.subTest(legacy=legacy):
                completed,_,_=self.readback(p,canonical,legacy=legacy)
                self.assertIn('saved_personalization_readback',completed)
                for key,snippet in canonical.items():
                    self.assertTrue(snippet.endswith('\n'))
                    observed={**canonical,key:snippet[:-1]}
                    with self.subTest(key=key),self.assertRaisesRegex(ValueError,'exact Mini snippet'):
                        self.readback(p,observed,legacy=legacy)

    def test_no_terminal_newline_payload_requires_exact_characters_and_line_boundaries(self):
        canonical={'custom_instructions':'Use exact guidance.\nKeep formats.',
                   'more_about_you':'[HELIKON_MINI_PROFILE_BEGIN]\nRuntime: fixture@1.\n[HELIKON_MINI_PROFILE_END]'}
        p={'system_layer':{'exact_install_text':canonical}}
        for key,snippet in canonical.items():
            cases={'interior_character':snippet.replace('i','I',1),
                   'interior_whitespace':snippet.replace('\n','\n ',1),
                   'prefix_without_separator':'unrelated '+snippet,
                   'suffix_without_separator':snippet+' unrelated',
                   'space_before_boundary':snippet+' \nLater preference.',
                   'partial_payload':snippet[:-1],
                   'normalized_line_endings':snippet.replace('\n','\r\n')}
            for case,observed in cases.items():
                with self.subTest(key=key,case=case),self.assertRaisesRegex(ValueError,'exact Mini snippet'):
                    self.readback(p,{**canonical,key:observed})
            for observed in (snippet,'Earlier preference.\n'+snippet,
                             snippet+'\nLater preference.',
                             'Earlier preference.\r\n'+snippet+'\r\nLater preference.'):
                with self.subTest(key=key,valid=observed):
                    completed,_,_=self.readback(p,{**canonical,key:observed})
                    self.assertIn('saved_personalization_readback',completed)

    def test_canonical_leading_and_trailing_spaces_are_not_trimmed(self):
        canonical={'custom_instructions':' Exact guidance. ',
                   'more_about_you':' Exact profile.\n'}
        p={'system_layer':{'exact_install_text':canonical}}
        for key,snippet in canonical.items():
            with self.subTest(key=key),self.assertRaisesRegex(ValueError,'exact Mini snippet'):
                self.readback(p,{**canonical,key:snippet.strip()})


if __name__=='__main__':unittest.main()
