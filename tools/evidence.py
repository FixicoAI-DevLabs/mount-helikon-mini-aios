#!/usr/bin/env python3
"""Validate submitted pilot records without treating self-reported passes as proof."""
import argparse
import datetime
import json
import sys
from pathlib import Path
from mini import ROOT, RUNTIME, SYSTEM, Invalid, load, require, sha, valid_sha256


def nonempty(value, label):
    require(isinstance(value,str) and bool(value.strip()), label+': nonempty string required')


def evidence_ref(ref, base):
    require(isinstance(ref,dict) and set(ref)=={'path','sha256','excerpt'}, 'Evidence reference fields invalid')
    nonempty(ref['path'],'Evidence path'); nonempty(ref['excerpt'],'Evidence excerpt')
    require(len(ref['excerpt'].strip())>=8, 'Evidence excerpt too short')
    relative=Path(ref['path'])
    require(not relative.is_absolute(), 'Evidence paths must be local relative paths')
    base=Path(base).resolve(); path=(base/relative).resolve()
    require(path.is_relative_to(base), 'Evidence path escapes record directory')
    require(path.is_file(), 'Referenced evidence file missing')
    data=path.read_bytes()
    require(sha(data)==ref['sha256'], 'Evidence hash mismatch')
    try: text=data.decode('utf-8')
    except UnicodeError as exc: raise Invalid('Evidence transcript must be UTF-8') from exc
    require(ref['excerpt'] in text, 'Cited excerpt absent from transcript')
    return ref['sha256']


def template():
    return {'format':'helikon-mini.pilot-record@1.0.0','record_state':'not_run',
            'profile':None,'host':{'client':None,'model':None,'plan':None,'observed_at':None},
            'expected_candidate':{'runtime_sha256':sha((ROOT/RUNTIME).read_bytes()),'system_sha256':sha((ROOT/SYSTEM).read_bytes())},
            'runs':[], 'supplementary':[], 'installation':[], 'utility':[],
            'limitations':['No live observations have been collected.'],
            'release_authorized':False}


def check_source_observation(observation, base):
    fields={'availability','runtime_body_observed','system_body_observed','runtime_sha256','system_sha256','evidence'}
    require(isinstance(observation,dict) and set(observation)==fields,'Invalid source observation fields')
    require(observation['availability'] in ['complete','missing','partial','mismatch','unknown'],'Invalid source availability')
    for key in ['runtime_body_observed','system_body_observed']:
        require(type(observation[key]) is bool,'Body observation must be Boolean')
    for key in ['runtime_sha256','system_sha256']:
        require(observation[key] is None or valid_sha256(observation[key]), 'Source hash must be null or lowercase SHA-256: '+key)
    for prefix in ['runtime','system']:
        require(not observation[prefix+'_body_observed'] or valid_sha256(observation[prefix+'_sha256']),
                'Observed complete body requires source hash: '+prefix)
    evidence_ref(observation['evidence'],base)
    expected=template()['expected_candidate']
    if observation['availability']=='complete':
        require(observation['runtime_body_observed'] and observation['system_body_observed'],'Complete requires both full body observations')
        require(observation['runtime_sha256']==expected['runtime_sha256'] and observation['system_sha256']==expected['system_sha256'],'Complete source hash mismatch')
    if observation['availability'] in ['missing','partial','unknown']:
        require(not observation['runtime_body_observed'] and observation['runtime_sha256'] is None,'Missing/partial/unknown source cannot claim complete runtime observation')
    if observation['availability']=='mismatch':
        require(valid_sha256(observation['runtime_sha256']) and observation['runtime_sha256'] != expected['runtime_sha256'],
                'Mismatch requires a different valid runtime hash')


def check_rows(rows, expected, base, label):
    require(isinstance(rows,list),label+': list required')
    seen=set(); failures=[]; digests=[]
    for row in rows:
        fields={'id','kind','reviewer','evidence','criteria'} | ({'source_observation'} if label=='runs' else set())
        require(isinstance(row,dict) and set(row)==fields,label+': invalid row fields')
        rid=row['id']; require(isinstance(rid,str) and rid in expected,label+': unknown run ID')
        require(rid not in seen,label+': duplicate run ID');seen.add(rid)
        require(row['kind']=='live_host','Synthetic observations cannot count as live pilot evidence')
        nonempty(row['reviewer'],'Reviewer')
        digest=evidence_ref(row['evidence'],base);digests.append(digest)
        if label=='runs':
            check_source_observation(row['source_observation'],base)
            condition=row['source_observation']['availability']
            case=rid.split('-')[0]
            if case=='B02':require(condition in ['missing','unknown'],'Missing-source case used an available runtime')
            elif case=='B03':require(condition in ['partial','mismatch'],'Wrong/partial-source case used complete runtime')
            elif case!='B04':require(condition=='complete','Positive case lacks exact complete candidate source')
        required=expected[rid]
        require(isinstance(row['criteria'],dict) and set(row['criteria'])==set(required),label+': criterion inventory mismatch')
        for criterion, finding in row['criteria'].items():
            require(isinstance(finding,dict) and set(finding)=={'met','excerpt'},'Invalid criterion finding')
            require(type(finding['met']) is bool,'Criterion outcome must be Boolean')
            ref=dict(row['evidence']);ref['excerpt']=finding['excerpt'];evidence_ref(ref,base)
            if not finding['met']:failures.append(rid+':'+criterion)
    require(seen==set(expected),label+': missing required runs')
    # Each independently fresh run needs its own transcript, not one copied receipt.
    require(len(digests)==len(set(digests)),label+': reused transcript across independent runs')
    return failures


def expected_runs():
    cases=load(ROOT/'tests/behavior/cases.json')['cases']
    behavior={f'{case}-{run}':value['criteria'] for case,value in cases.items() for run in range(1,4)}
    supplementary={key:['observed_result','acceptance_met'] for key in ['B03-wrong','B03-partial','B11-code','B11-csv','B11-template']}
    installation={key:['existing_state_recorded','scope_covered','result_observed','recovery_assessed'] for key in ['clean','existing-settings','legacy-residue','interrupted','duplicate-request','recovery','fresh-chat']}
    utility_doc=load(ROOT/'tests/behavior/utility.json')
    utility={f"{task['id']}-{condition}-{run}":['task_completed','no_checkable_error','format_met'] for task in utility_doc['tasks'] for condition in utility_doc['conditions'] for run in range(1,4)}
    return behavior,supplementary,installation,utility


def validate_record(record,base):
    require(set(record)==set(template()),'Record fields invalid; status/pass labels are not accepted')
    require(record['format']=='helikon-mini.pilot-record@1.0.0','Wrong evidence format')
    require(record['release_authorized'] is False,'An evidence record cannot authorize release')
    require(record['expected_candidate']==template()['expected_candidate'],'Candidate bytes differ')
    require(isinstance(record['limitations'],list) and all(isinstance(x,str) and x.strip() for x in record['limitations']),'Invalid limitations')
    require(record['record_state'] in ['not_run','collected'],'Invalid record state')
    if record['record_state']=='not_run':
        require(not any(record[k] for k in ['runs','supplementary','installation','utility']),'Not-run record contains asserted observations')
        require(record['profile'] is None and record['host']==template()['host'],'Not-run record contains asserted host state')
        return {'status':'not_run','release_ready':False,'scope':'empty_pilot_template_only'}
    profiles=load(ROOT/'profiles/chatgpt/profiles.json')['profiles']
    require(record['profile'] in [p['id'] for p in profiles],'Unknown profile')
    require(isinstance(record['host'],dict) and set(record['host'])==set(template()['host']),'Host context invalid')
    for key,value in record['host'].items():nonempty(value,'Host '+key)
    try:
        observed=datetime.datetime.fromisoformat(record['host']['observed_at'].replace('Z','+00:00'))
        require(observed.tzinfo is not None,'Host observation needs timezone')
    except ValueError as exc:raise Invalid('Host observation time invalid') from exc
    failures=[]
    for name,expected in zip(['runs','supplementary','installation','utility'],expected_runs()):
        failures+=check_rows(record[name],expected,base,name)
    return {'status':'record_consistent_manual_review_required','release_ready':False,
            'failed_criteria':failures,'counts':{k:len(record[k]) for k in ['runs','supplementary','installation','utility']},
            'limits':['File integrity and record consistency do not authenticate host observations or reviewer judgments.',
                      'Utility benefits/costs and failures require substantive review; this tool supplies no release verdict.']}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest='command',required=True)
    prep=sub.add_parser('template');prep.add_argument('--out',required=True)
    check=sub.add_parser('validate');check.add_argument('record')
    args=parser.parse_args()
    try:
        if args.command=='template':
            path=Path(args.out);require(not path.exists(),'Refusing to overwrite an existing evidence record')
            path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(template(),indent=2)+'\n')
            result={'status':'prepared_not_run','path':str(path),'release_ready':False}
        else: result=validate_record(load(args.record),Path(args.record).parent)
        print(json.dumps(result,indent=2))
        if result['status']=='not_run':sys.exit(2)
    except (Invalid,OSError,ValueError,KeyError,TypeError) as exc:
        print(json.dumps({'status':'invalid','error':str(exc),'release_ready':False}));sys.exit(1)
