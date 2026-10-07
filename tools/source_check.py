#!/usr/bin/env python3
"""Verify the source inventory against an explicitly supplied authorized master."""
import argparse
import json
import sys
from pathlib import Path
from mini import ROOT, Invalid, canonical, load, require, resolve, sha, validate_source_inventory


def atomic_ids(value):
    result=[]
    if isinstance(value, dict):
        if isinstance(value.get('id'),str) and ('statement' in value or 'instruction' in value):
            result.append(value['id'])
        for child in value.values():
            result += atomic_ids(child)
    elif isinstance(value,list):
        for child in value:
            result += atomic_ids(child)
    return result


def verify_source(path, root=ROOT):
    root=Path(root)
    data=Path(path).read_bytes(); master=load(path)
    mapping=validate_source_inventory(root)
    index=load(root/'docs/source-index.json')
    provenance=load(root/'docs/source-manifest.json')['source']
    require(sha(data)==index['source_sha256']==mapping['source_sha256'], 'Wrong full source hash')
    for key in ['runtime','schema','system_contract']:
        require(master['identity'][key]==provenance[key], 'Full source identity mismatch: '+key)
    pointers=[]
    for key,value in master.items():
        if key in ['bootstrap','owners','routing'] or not isinstance(value,dict):
            pointers.append('#/'+key)
        else:
            pointers.extend('#/'+key+'/'+name for name in value)
    require(pointers==index['pointers'], 'Source component inventory/order differs')
    ids=[]
    for row in mapping['entries']:
        node=resolve(master,row['source_pointer'])
        require(sha(canonical(node))==row['source_sha256'], 'Source component changed: '+row['source_pointer'])
        require(atomic_ids(node)==row['source_rule_ids'], 'Normative ID inventory mismatch')
        ids.extend(atomic_ids(node))
    require(ids==index['normative_ids'], 'Normative index mismatch')
    return {'status':'pass','scope':'source_identity_and_inventory_only','components':len(pointers),'normative_ids':len(ids),'semantic_equivalence':'not_asserted'}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('master')
    args=parser.parse_args()
    try:
        print(json.dumps(verify_source(args.master),indent=2))
    except (Invalid,OSError,ValueError,KeyError,TypeError) as exc:
        print(json.dumps({'status':'fail','error':str(exc)}));sys.exit(1)
