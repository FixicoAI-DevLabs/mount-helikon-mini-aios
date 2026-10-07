#!/usr/bin/env python3
"""Build the guided installer and check installation records; never change an account."""
import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = Path('Helikon_Mini_Install_Package.json')
SYSTEM = Path('installer/custom_instructions.txt')
PROFILE = Path('installer/more_about_you.txt')
RUNTIME = Path('Helikon_Mini_Operating_Master.json')
RECORD_VERSION = '2.0.0'
STATUSES = {'not_run', 'unknown', 'failed', 'passed'}
METHODS = {'not_recorded', 'direct_observation', 'user_reported'}
BEHAVIOR_IDS = ('exact_json', 'duration_capacity', 'missing_source', 'wrong_source')
CHECKPOINT_IDS = ('exact_package_read', 'existing_settings_backed_up',
                  'runtime_extracted_and_checked', 'runtime_saved_and_read_from_library',
                  'custom_instructions_saved_and_read_back', 'more_about_you_saved_and_read_back',
                  'fresh_ordinary_chat_without_attachment_source_read', 'ordinary_chat_behavior_checked')
HANDOFF_BEGIN = '<!-- FRESH_CHAT_HANDOFF_BEGIN -->'
HANDOFF_END = '<!-- FRESH_CHAT_HANDOFF_END -->'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def package(root=ROOT):
    root = Path(root)
    # Text-mode reads normalize CRLF. Preserve the actual distributed UTF-8 bytes.
    runtime_bytes = (root/RUNTIME).read_bytes()
    runtime_text = runtime_bytes.decode('utf-8')
    runtime = json.loads(runtime_text)
    snippets = {key:(root/path).read_bytes().decode('utf-8') for key,path in
                [('custom_instructions', SYSTEM), ('more_about_you', PROFILE)]}
    return {
        'schema_id':'helikon_mini.install_package', 'schema_version':'2.1.0',
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
                           'sha256':sha(runtime_bytes),
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
            'retain each Mini snippet verbatim and stop until the combined field fits; never truncate silently. '
            'Only add a source ID when the host actually returns it.\n')


def render(root=ROOT):
    root=Path(root);p=package(root)
    (root/PACKAGE).write_bytes((json.dumps(p,indent=2,ensure_ascii=False)+'\n').encode('utf-8'))
    (root/'Helikon_Mini_System.md').write_bytes(system_markdown(p).encode('utf-8'))
    return p


def validate(root=ROOT):
    root=Path(root);actual=read_json(root/PACKAGE);expected=package(root)
    if actual!=expected:raise ValueError('Stale or modified unified installation package')
    if (root/'Helikon_Mini_System.md').read_bytes()!=system_markdown(expected).encode('utf-8'):
        raise ValueError('System projection differs from canonical snippets')
    texts=expected['system_layer']['exact_install_text']
    if set(texts)!={'custom_instructions','more_about_you'} or any(len(t)>1500 for t in texts.values()):
        raise ValueError('Two separate bounded Personalization snippets required')
    profile = texts['more_about_you']
    begin = '[HELIKON_MINI_PROFILE_BEGIN]'; end = '[HELIKON_MINI_PROFILE_END]'
    if profile.count(begin) != 1 or profile.count(end) != 1 or profile.index(begin) >= profile.index(end):
        raise ValueError('Profile binding block markers differ')
    lines = profile.split(begin, 1)[1].split(end, 1)[0].splitlines()
    operating = expected['operating_layer']
    bindings = {'SHA-256':operating['sha256']}
    for label, key in (('Runtime', 'runtime'), ('Schema', 'schema'),
                       ('System contract', 'system_contract'), ('Extension contract', 'extension_contract')):
        pair = operating['identity'][key]
        bindings[label] = pair['id']+'@'+pair['version']+'.'
    for label, value in bindings.items():
        # Require one exact designation line, not a matching substring beside a
        # conflicting or stale binding. Rendering never rewrites designations.
        found = [line for line in lines if line.lstrip().startswith(label+':')]
        if found != [label+': '+value]:
            raise ValueError('Profile '+label+' binding differs from exact runtime')
    contract=expected['installer']
    if contract['primary_surface']!='ordinary_non_project_chat' or contract['projects_required']:
        raise ValueError('Project-only installation is not Mini account installation')
    if contract['source']['storage']!='account_library' or contract['source']['memory_writes_required']:
        raise ValueError('Operating delivery must use JSON, not memory records')
    required={'SETUP','INSTALL','EXTRACT','NEXT','FINAL_VERIFY','STATUS','RESTORE','REMEMBER'}
    if set(contract['commands'])!=required:raise ValueError('Installer command inventory differs')
    if not contract['preserve_existing_settings'] or not contract['protect_active_full_helikon']:
        raise ValueError('Existing configuration protection is required')
    if tuple(contract.get('checkpoints', ())) != CHECKPOINT_IDS:
        raise ValueError('Eight ordered installation checkpoints required')
    personalization = contract.get('personalization_contract', {})
    budgets = personalization.get('snippet_design_budgets', {})
    if personalization.get('exact_snippets_required') is not True or set(budgets) != set(texts):
        raise ValueError('Exact Personalization snippets and design budgets required')
    if any(type(budgets[key]) is not int or not 0 < budgets[key] <= 1500 or len(texts[key]) > budgets[key]
           for key in texts):
        raise ValueError('Personalization snippet exceeds its design budget')
    handoff = contract.get('fresh_chat_handoff', {})
    if (handoff.get('surface') != 'fresh_ordinary_non_project_non_temporary_chat'
            or handoff.get('attachments_allowed') is not False or not _text(handoff.get('prompt'))):
        raise ValueError('Self-contained fresh-chat handoff without attachments required')
    expected_block = '\n```text\n'+handoff['prompt']+'\n```\n'
    for relative in ('START_HERE.md', 'Helikon_Mini_QA.md', 'docs/install.md'):
        path = root/relative
        if relative == 'docs/install.md' and (not path.exists() or HANDOFF_BEGIN not in path.read_text()):
            continue
        text = path.read_bytes().decode('utf-8')
        if text.count(HANDOFF_BEGIN) != 1 or text.count(HANDOFF_END) != 1:
            raise ValueError('Fresh-chat handoff marker inventory differs: '+relative)
        block = text.split(HANDOFF_BEGIN, 1)[1].split(HANDOFF_END, 1)[0]
        if block != expected_block:
            raise ValueError('Fresh-chat handoff projection differs: '+relative)
    return {'status':'pass','scope':'installer_artifact_consistency_only',
            'live_installation':'not_evaluated','characters':{k:len(v) for k,v in texts.items()}}


def record_template(root=ROOT):
    p = package(root)
    checkpoint = lambda: {'status':'not_run', 'observation_method':'not_recorded',
                          'evidence':[], 'notes':''}
    return {'record_version':RECORD_VERSION, 'package_version':p['package_version'],
            'installer_protocol_version':p['installer']['protocol_version'],
            'host':{'client':None, 'plan':None, 'model':None, 'observed_at':None,
                    'observation_method':'not_recorded', 'evidence':None},
            'checkpoints':{name:checkpoint() for name in p['installer']['checkpoints']},
            'backup':{'status':'not_run', 'observation_method':'not_recorded',
                      'exact_backup_exists':None, 'storage_description':None, 'evidence':None},
            'surface':None, 'settings_readback':None, 'runtime_readback':None,
            'ordinary_chat_readback':None,
            'behavior_results':[{'id':name, 'status':'not_run',
                                 'observation_method':'not_recorded', 'evidence':None}
                                for name in BEHAVIOR_IDS],
            'limitations':['No account installation observations recorded.']}


def _fields(value, names, label):
    if not isinstance(value, dict) or set(value) != set(names):
        raise ValueError(label+' fields differ')


def _text(value):
    return isinstance(value, str) and bool(value.strip())


def _evidence_reader(base):
    base = Path(base).resolve()
    def evidence(ref):
        _fields(ref, ('path', 'sha256', 'excerpt'), 'Evidence reference')
        if not all(_text(ref[key]) for key in ref):
            raise ValueError('Evidence reference values must be nonempty text')
        relative = Path(ref['path'])
        if relative.is_absolute():
            raise ValueError('Evidence path must be relative to the record directory')
        path = (base/relative).resolve()
        if not path.is_relative_to(base):
            raise ValueError('Evidence path escapes record directory')
        data = path.read_bytes()
        if sha(data) != ref['sha256'] or ref['excerpt'] not in data.decode('utf-8'):
            raise ValueError('Evidence bytes or excerpt mismatch')
        return data
    return evidence


def _observation_method(method, label, required=False):
    if not isinstance(method, str) or method not in METHODS or (required and method == 'not_recorded'):
        raise ValueError(label+' needs a valid observation method')


def _readbacks(record, p, evidence, legacy=False):
    completed = []; missing = []; reported = []
    if record['surface'] != 'ordinary_non_project_chat':
        missing.append('ordinary_non_project_chat')
    settings = record['settings_readback']
    if settings is None:
        missing.append('saved_personalization_readback')
    else:
        keys = {'custom_instructions', 'more_about_you', 'evidence', 'unrelated_content_preserved'}
        if not legacy: keys.add('observation_method')
        _fields(settings, keys, 'Settings observation')
        if not legacy:
            _observation_method(settings['observation_method'], 'Settings', required=True)
            if settings['observation_method'] == 'user_reported': reported.append('settings_readback')
        evidence(settings['evidence'])
        for key, text in p['system_layer']['exact_install_text'].items():
            if not isinstance(settings[key], str) or text.strip() not in settings[key]:
                raise ValueError('Saved settings omit exact Mini snippet')
        if settings['unrelated_content_preserved'] is not True:
            raise ValueError('Existing content not preserved')
        completed.append('saved_personalization_readback')
    for key in ('runtime_readback', 'ordinary_chat_readback'):
        obs = record[key]
        if obs is None:
            missing.append(key); continue
        keys = {'source_ref', 'full_runtime_file', 'evidence', 'surface', 'source_method'}
        if not legacy: keys.add('observation_method')
        _fields(obs, keys, 'Source observation')
        if not legacy:
            _observation_method(obs['observation_method'], key, required=True)
            if obs['observation_method'] == 'user_reported': reported.append(key)
        if not _text(obs['source_ref']) or obs['source_method'] not in ('supported_file_read', 'bounded_exact_source_copy'):
            raise ValueError('Actual source reference/read method required')
        evidence(obs['evidence'])
        raw = evidence(obs['full_runtime_file'])
        if sha(raw) != p['operating_layer']['sha256']:
            raise ValueError('Runtime readback differs')
        if key == 'runtime_readback' and obs['surface'] != 'account_library':
            raise ValueError('Saved runtime must be read back from account Library')
        if key == 'ordinary_chat_readback' and obs['surface'] != 'fresh_ordinary_non_project_chat_without_attachment':
            raise ValueError('Project, Work or attached-file tests cannot establish ordinary-chat automatic access')
        completed.append(key)
    return completed, missing, reported


def _legacy_record(record, p, evidence):
    _fields(record, ('record_version', 'package_version', 'surface', 'settings_readback',
                     'runtime_readback', 'ordinary_chat_readback', 'behavior_results', 'limitations'),
            'Installation record')
    # Historical versions cannot be checked against today's snippets/runtime. Do not
    # silently migrate them or relabel their old observations as current acceptance.
    if record['package_version'] != p['package_version']:
        return {'status':'legacy_record_requires_matching_package', 'record_version':'1.0.0',
                'missing_or_failed':['current_version_host_metadata_checkpoints_and_backup'],
                'release_ready':False,
                'limit':'Historical record retained; verify its bytes with its matching historical package.'}
    completed, missing, _ = _readbacks(record, p, evidence, legacy=True)
    rows = record['behavior_results']
    if not isinstance(rows, list): raise ValueError('Behavior results must be a list')
    ids = []
    for row in rows:
        _fields(row, ('id', 'passed', 'evidence'), 'Legacy behavior observation')
        if row['id'] not in BEHAVIOR_IDS or type(row['passed']) is not bool:
            raise ValueError('Invalid legacy behavior observation')
        evidence(row['evidence']); ids.append(row['id'])
        if not row['passed']: missing.append('failed:'+row['id'])
    if len(ids) != len(set(ids)): raise ValueError('Duplicate behavior observation')
    missing += sorted(set(BEHAVIOR_IDS)-set(ids))
    missing.append('current_version_host_metadata_checkpoints_and_backup')
    return {'status':'legacy_record_manual_review_required', 'record_version':'1.0.0',
            'completed_observations':completed, 'missing_or_failed':missing,
            'release_ready':False, 'limit':'Legacy observations do not satisfy the current installation record contract.'}


def verify_record(record, base, root=ROOT):
    """Check evidence bytes and recorded scope, never independently authenticate a host."""
    p = package(root); evidence = _evidence_reader(base)
    if not isinstance(record, dict): raise ValueError('Installation record must be an object')
    if not isinstance(record.get('limitations'), list) or not all(isinstance(v, str) for v in record['limitations']):
        raise ValueError('Limitations must be a list of text observations')
    if record.get('record_version') == '1.0.0':
        return _legacy_record(record, p, evidence)
    _fields(record, record_template(root), 'Installation record')
    if record['record_version'] != RECORD_VERSION: raise ValueError('Wrong installation record version')
    if record['package_version'] != p['package_version']: raise ValueError('Wrong installer version')
    if record['installer_protocol_version'] != p['installer']['protocol_version']:
        raise ValueError('Wrong installer protocol version')
    completed, missing, reported = _readbacks(record, p, evidence)
    host = record['host']
    _fields(host, ('client', 'plan', 'model', 'observed_at', 'observation_method', 'evidence'), 'Host metadata')
    _observation_method(host['observation_method'], 'Host metadata')
    for key in ('client', 'plan', 'model', 'observed_at'):
        value = host[key]
        if value is not None and not _text(value): raise ValueError('Host metadata values must be text or null')
        if value is None: missing.append('host:'+key)
    if host['observed_at'] is not None:
        try:
            observed = datetime.fromisoformat(host['observed_at'].replace('Z', '+00:00'))
            if observed.tzinfo is None: raise ValueError('timezone missing')
        except ValueError as exc:
            raise ValueError('Host observed_at must be an ISO-8601 timestamp with timezone') from exc
    if host['evidence'] is not None: evidence(host['evidence'])
    else: missing.append('host:evidence')
    if host['observation_method'] == 'not_recorded': missing.append('host:observation_method')
    if host['observation_method'] == 'user_reported': reported.append('host_metadata')

    def state(row, label):
        if not isinstance(row['status'], str) or row['status'] not in STATUSES:
            raise ValueError(label+' has invalid status')
        _observation_method(row['observation_method'], label, required=row['status'] in {'passed', 'failed'})
        if row['status'] != 'passed': missing.append(row['status']+':'+label)
        if row['observation_method'] == 'user_reported': reported.append(label)

    checkpoints = record['checkpoints']
    _fields(checkpoints, p['installer']['checkpoints'], 'Checkpoint inventory')
    for name, row in checkpoints.items():
        _fields(row, ('status', 'observation_method', 'evidence', 'notes'), 'Checkpoint observation')
        if not isinstance(row['notes'], str): raise ValueError('Checkpoint notes must be text')
        state(row, name)
        if not isinstance(row['evidence'], list): raise ValueError('Checkpoint evidence must be a list')
        if row['status'] in {'passed', 'failed'} and not row['evidence']:
            raise ValueError('Observed checkpoint needs evidence')
        for ref in row['evidence']: evidence(ref)
        if row['status'] == 'passed': completed.append('checkpoint:'+name)

    backup = record['backup']
    _fields(backup, ('status', 'observation_method', 'exact_backup_exists', 'storage_description', 'evidence'), 'Backup')
    state(backup, 'exact_settings_backup')
    if backup['exact_backup_exists'] is not None and type(backup['exact_backup_exists']) is not bool:
        raise ValueError('Backup existence must be a boolean or null')
    if backup['storage_description'] is not None and not _text(backup['storage_description']):
        raise ValueError('Backup storage description must be text or null')
    if backup['evidence'] is not None: evidence(backup['evidence'])
    elif backup['status'] in {'passed', 'failed'}: raise ValueError('Observed backup needs evidence')
    if backup['status'] == 'passed' and (backup['exact_backup_exists'] is not True or not _text(backup['storage_description'])):
        raise ValueError('Passed backup needs an exact stored backup')

    rows = record['behavior_results']
    if not isinstance(rows, list): raise ValueError('Behavior results must be a list')
    ids = []
    for row in rows:
        _fields(row, ('id', 'status', 'observation_method', 'evidence'), 'Behavior observation')
        if row['id'] not in BEHAVIOR_IDS: raise ValueError('Invalid behavior observation ID')
        state(row, row['id']); ids.append(row['id'])
        if row['evidence'] is not None: evidence(row['evidence'])
        elif row['status'] in {'passed', 'failed'}: raise ValueError('Observed behavior needs evidence')
    if len(ids) != len(set(ids)): raise ValueError('Duplicate behavior observation')
    if set(ids) != set(BEHAVIOR_IDS): raise ValueError('Behavior inventory differs; retain explicit not_run rows')
    return {'status':'incomplete' if missing else 'record_consistent_manual_review_required',
            'record_version':RECORD_VERSION, 'completed_observations':completed,
            'missing_or_failed':missing, 'user_reported_observations':reported,
            'release_ready':False,
            'limit':'Evidence consistency is not independent host authentication or release authority; semantic review remains required.'}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('render'); sub.add_parser('validate')
    t = sub.add_parser('record-template'); t.add_argument('--out', required=True)
    v = sub.add_parser('verify-record'); v.add_argument('record')
    args = parser.parse_args(argv)
    try:
        if args.command == 'render':
            render(); result = {'status':'generated'}
        elif args.command == 'validate': result = validate()
        elif args.command == 'record-template':
            content = json.dumps(record_template(), indent=2)+'\n'
            path = Path(args.out); path.parent.mkdir(parents=True, exist_ok=True)
            # Exclusive creation is atomic; a repeated command never erases evidence.
            with path.open('x', encoding='utf-8', newline='\n') as stream:
                stream.write(content)
            result = {'status':'not_run', 'path':str(path)}
        else:
            path = Path(args.record); result = verify_record(read_json(path), path.parent)
    except (ValueError, OSError) as exc:
        print(json.dumps({'status':'invalid', 'error':str(exc), 'release_ready':False}, indent=2))
        return 1
    print(json.dumps(result, indent=2))
    if args.command == 'verify-record' and result['status'] != 'record_consistent_manual_review_required':
        return 2
    return 0


if __name__ == '__main__': sys.exit(main())
