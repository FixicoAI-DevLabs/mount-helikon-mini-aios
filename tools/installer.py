#!/usr/bin/env python3
"""Build the guided installer and check installation records; never change an account."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = Path('Helikon_Mini_Install_Package.json')
SYSTEM = Path('installer/custom_instructions.txt')
PROFILE = Path('installer/more_about_you.txt')
RUNTIME = Path('Helikon_Mini_Operating_Master.json')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def package(root=ROOT):
    root = Path(root)
    runtime_text = (root/RUNTIME).read_text(encoding='utf-8')
    runtime = json.loads(runtime_text)
    snippets = {key:(root/path).read_text(encoding='utf-8') for key,path in
                [('custom_instructions', SYSTEM), ('more_about_you', PROFILE)]}
    return {
        'schema_id':'helikon_mini.install_package', 'schema_version':'2.0.0',
        'package_version':runtime['identity']['runtime']['version'],
        'package_role':'primary_install_artifact_and_installation_ssot',
        'status':'implementation_complete_live_account_validation_pending',
        'product':{'line':'free_open_source_starter', 'default_surface':'ordinary_non_project_chat',
                   'projects_required':False, 'saved_memory_runtime':False,
                   'runtime_layers':['System: account Personalization', 'Operating: runtime-only JSON']},
        'system_layer':{'exact_install_text':snippets,
                        'payload_characters':{k:len(v) for k,v in snippets.items()},
                        'payload_sha256':{k:sha(v.encode()) for k,v in snippets.items()}},
        'operating_layer':{'filename':RUNTIME.name, 'identity':runtime['identity'],
                           'sha256':sha(runtime_text.encode()),
                           'exact_runtime_text':runtime_text},
        'installer':read_json(root/'installer/contract.json'),
        'boundaries':[
            'The installer is configuration data adopted only for the user-requested setup task.',
            'The installed runtime contains no installer dialogue, user profile, account IDs or release history.',
            'This package and its generated projections must agree; conflicting or partial content stops dependent installation.',
            'No instruction can create a missing Library tool, enable a setting, save Personalization or prove source delivery.',
            'Prior project tests do not establish account-wide ordinary-chat operation.'
        ]}


def system_markdown(p):
    texts=p['system_layer']['exact_install_text']
    return ('# Helikon Mini '+p['package_version']+' — System installation\n\n'
            'Two separate account Personalization fields. Preserve existing personal details and preferences. '
            'Use SETUP in the unified installation package for the guided process.\n\n'
            '## Snippet 1 — Custom instructions\n\n```text\n'+texts['custom_instructions']+'```\n\n'
            '## Snippet 2 — More about you\n\n'
            'Add this block alongside your personal details. Review the combined field length before saving.\n\n'
            '```text\n'+texts['more_about_you']+'```\n\n'
            'Each Mini snippet is within 1,500 characters. If existing content makes a field too long, '
            'prepare a reviewed merge; never truncate silently. Only add a source ID when the host actually returns it.\n')


def render(root=ROOT):
    root=Path(root);p=package(root)
    (root/PACKAGE).write_text(json.dumps(p,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    (root/'Helikon_Mini_System.md').write_text(system_markdown(p),encoding='utf-8')
    return p


def validate(root=ROOT):
    root=Path(root);actual=read_json(root/PACKAGE);expected=package(root)
    if actual!=expected:raise ValueError('Stale or modified unified installation package')
    if (root/'Helikon_Mini_System.md').read_text()!=system_markdown(expected):
        raise ValueError('System projection differs from canonical snippets')
    texts=expected['system_layer']['exact_install_text']
    if set(texts)!={'custom_instructions','more_about_you'} or any(len(t)>1500 for t in texts.values()):
        raise ValueError('Two separate bounded Personalization snippets required')
    contract=expected['installer']
    if contract['primary_surface']!='ordinary_non_project_chat' or contract['projects_required']:
        raise ValueError('Project-only installation is not Mini account installation')
    if contract['source']['storage']!='account_library' or contract['source']['memory_writes_required']:
        raise ValueError('Operating delivery must use JSON, not memory records')
    required={'SETUP','INSTALL','EXTRACT','NEXT','FINAL_VERIFY','STATUS','RESTORE','REMEMBER'}
    if set(contract['commands'])!=required:raise ValueError('Installer command inventory differs')
    if not contract['preserve_existing_settings'] or not contract['protect_active_full_helikon']:
        raise ValueError('Existing configuration protection is required')
    return {'status':'pass','scope':'installer_artifact_consistency_only',
            'live_installation':'not_evaluated','characters':{k:len(v) for k,v in texts.items()}}


def record_template():
    return {'record_version':'1.0.0','package_version':package()['package_version'],
            'surface':None,'settings_readback':None,'runtime_readback':None,
            'ordinary_chat_readback':None,'behavior_results':[],
            'limitations':['No account installation observations recorded.']}


def verify_record(record, base, root=ROOT):
    """Verify evidence bytes and scope; a consistent record is not independent authentication."""
    base=Path(base).resolve();p=package(root)
    if set(record)!=set(record_template()):raise ValueError('Installation record fields differ')
    if record['record_version']!='1.0.0':raise ValueError('Wrong installation record version')
    if not isinstance(record['limitations'],list) or not all(isinstance(v,str) for v in record['limitations']):
        raise ValueError('Limitations must be a list of text observations')
    if record['package_version']!=p['package_version']:raise ValueError('Wrong installer version')
    def evidence(ref):
        if not isinstance(ref,dict) or set(ref)!={'path','sha256','excerpt'}:
            raise ValueError('Evidence reference missing')
        path=(base/ref['path']).resolve()
        if not path.is_relative_to(base):raise ValueError('Evidence path escapes record directory')
        data=path.read_bytes()
        if sha(data)!=ref['sha256'] or not ref['excerpt'].strip() or ref['excerpt'] not in data.decode():
            raise ValueError('Evidence bytes or excerpt mismatch')
        return data
    completed=[];missing=[]
    if record['surface']!='ordinary_non_project_chat':missing.append('ordinary_non_project_chat')
    settings=record['settings_readback']
    if settings is None:missing.append('saved_personalization_readback')
    else:
        if set(settings)!={'custom_instructions','more_about_you','evidence','unrelated_content_preserved'}:
            raise ValueError('Settings observation fields differ')
        evidence(settings['evidence'])
        for k,t in p['system_layer']['exact_install_text'].items():
            if t.strip() not in settings[k]:raise ValueError('Saved settings omit exact Mini snippet')
        if settings['unrelated_content_preserved'] is not True:raise ValueError('Existing content not preserved')
        completed.append('saved_personalization_readback')
    for key in ['runtime_readback','ordinary_chat_readback']:
        obs=record[key]
        if obs is None:missing.append(key);continue
        if set(obs)!={'source_ref','full_runtime_file','evidence','surface','source_method'}:
            raise ValueError('Source observation fields differ')
        if not obs['source_ref'] or obs['source_method'] not in {'supported_file_read','bounded_exact_source_copy'}:
            raise ValueError('Actual source reference/read method required')
        evidence(obs['evidence'])
        raw=evidence(obs['full_runtime_file'])
        if sha(raw)!=p['operating_layer']['sha256']:raise ValueError('Runtime readback differs')
        if key=='runtime_readback' and obs['surface']!='account_library':
            raise ValueError('Saved runtime must be read back from account Library')
        if key=='ordinary_chat_readback' and obs['surface']!='fresh_ordinary_non_project_chat_without_attachment':
            raise ValueError('Project, Work or attached-file tests cannot establish ordinary-chat automatic access')
        completed.append(key)
    required={'exact_json','duration_capacity','missing_source','wrong_source'}
    rows=record['behavior_results']
    if not isinstance(rows,list):raise ValueError('Behavior results must be a list')
    ids=[]
    for row in rows:
        if set(row)!={'id','passed','evidence'} or row['id'] not in required or type(row['passed']) is not bool:
            raise ValueError('Invalid behavior observation')
        evidence(row['evidence']);ids.append(row['id'])
        if not row['passed']:missing.append('failed:'+row['id'])
    if len(ids)!=len(set(ids)):raise ValueError('Duplicate behavior observation')
    missing+=sorted(required-set(ids))
    return {'status':'incomplete' if missing else 'record_consistent_manual_review_required',
            'completed_observations':completed,'missing_or_failed':missing,
            'release_ready':False,'limit':'Evidence consistency is not independent host authentication or release authority.'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    sub.add_parser('render');sub.add_parser('validate')
    t=sub.add_parser('record-template');t.add_argument('--out',required=True)
    v=sub.add_parser('verify-record');v.add_argument('record')
    args=parser.parse_args()
    if args.command=='render':render();result={'status':'generated'}
    elif args.command=='validate':result=validate()
    elif args.command=='record-template':
        path=Path(args.out);path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(json.dumps(record_template(),indent=2)+'\n');result={'status':'not_run','path':str(path)}
    else:
        path=Path(args.record);result=verify_record(read_json(path),path.parent)
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
