"""Protect the restored account installation contract and reject false evidence scopes."""
import copy
import json
import shutil
import sys
import tempfile
import unittest
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
                'evidence':self.ref,'surface':surface,'source_method':'supported_file_read'}

    def complete_synthetic_record(self):
        record=installer.record_template();record['surface']='ordinary_non_project_chat'
        texts=installer.package()['system_layer']['exact_install_text']
        record['settings_readback']={**texts,'evidence':self.save('settings.txt','\n'.join(texts.values())),
                                     'unrelated_content_preserved':True}
        record['runtime_readback']=self.observation('account_library')
        record['ordinary_chat_readback']=self.observation('fresh_ordinary_non_project_chat_without_attachment')
        record['behavior_results']=[{'id':i,'passed':True,'evidence':self.ref} for i in
                                    ['exact_json','duration_capacity','missing_source','wrong_source']]
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

    def test_invented_pass_flag_rejected(self):
        record=installer.record_template();record['release_ready']=True
        with self.assertRaisesRegex(ValueError,'fields differ'):installer.verify_record(record,self.base)

    def test_failed_behavior_remains_incomplete(self):
        record=self.complete_synthetic_record();record['behavior_results'][0]['passed']=False
        result=installer.verify_record(record,self.base)
        self.assertEqual(result['status'],'incomplete');self.assertIn('failed:exact_json',result['missing_or_failed'])

    def test_changed_evidence_rejected(self):
        record=self.complete_synthetic_record();(self.base/'transcript.txt').write_text('changed')
        with self.assertRaisesRegex(ValueError,'mismatch'):installer.verify_record(record,self.base)


if __name__=='__main__':unittest.main()
