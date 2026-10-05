#!/usr/bin/env python3
"""Offline candidate validation, projection and packaging. Python standard library only.

These checks validate artifacts and recorded evidence, not model obedience or host state.
"""
import argparse
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = Path('src/runtime/Helikon_Mini_Operating_Master.json')
SYSTEM = Path('src/system/Helikon_Mini_System.md')
SCHEMA = Path('schema/Helikon_Mini_Operating_Master.schema.json')
PROJECTION = Path('generated/Helikon_Mini_Operating.md')


class Invalid(ValueError):
    pass


def sha(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def strict_json(text):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise Invalid('Duplicate JSON key: ' + key)
            result[key] = value
        return result
    def constant(value):
        raise Invalid('Nonfinite JSON number: ' + value)
    return json.loads(text, object_pairs_hook=pairs, parse_constant=constant)


def load(path):
    return strict_json(Path(path).read_text(encoding='utf-8'))


def require(condition, message):
    if not condition:
        raise Invalid(message)


def validate_schema(value, schema, path='$'):
    """Validate the deliberately small closed subset used by this checked-in schema.

    Unknown keywords are errors, never silently ignored. This is not a general
    JSON Schema implementation. The published schema also works with a full
    Draft 2020-12 validator. Boolean equality is deliberately type-sensitive.
    """
    allowed = {'$schema', '$id', 'title', 'description', 'type', 'const', 'properties',
               'required', 'additionalProperties', 'items', 'minItems', 'minLength'}
    require(not set(schema) - allowed, path + ': unsupported schema keyword')
    if 'const' in schema:
        require(canonical(value) == canonical(schema['const']), path + ': const mismatch')
    types = {'object': dict, 'array': list, 'string': str, 'boolean': bool,
             'integer': int, 'null': type(None)}
    if 'type' in schema:
        require(schema['type'] in types, path + ': unsupported schema type')
        require(type(value) is types[schema['type']], path + ': wrong type')
    if isinstance(value, dict):
        props = schema.get('properties', {})
        require(set(schema.get('required', [])) <= set(value), path + ': required key missing')
        if schema.get('additionalProperties') is False:
            require(set(value) <= set(props), path + ': unknown property')
        for k, child in value.items():
            if k in props:
                validate_schema(child, props[k], path + '/' + k)
    if isinstance(value, list):
        require(len(value) >= schema.get('minItems', 0), path + ': too few items')
        if 'items' in schema:
            for i, child in enumerate(value):
                validate_schema(child, schema['items'], path + '/' + str(i))
    if isinstance(value, str) and 'minLength' in schema:
        require(len(value) >= schema['minLength'] and bool(value.strip()), path + ': empty text')


def resolve(doc, ref):
    require(isinstance(ref, str) and ref.startswith('#/'), 'Nonlocal reference: ' + str(ref))
    node = doc
    try:
        for segment in ref[2:].split('/'):
            segment = segment.replace('~1', '/').replace('~0', '~')
            node = node[int(segment)] if isinstance(node, list) else node[segment]
    except (KeyError, IndexError, TypeError, ValueError) as exc:
        raise Invalid('Unresolved reference: ' + ref) from exc
    return node


def refs(node):
    if isinstance(node, dict):
        for value in node.values():
            yield from refs(value)
    elif isinstance(node, list):
        for value in node:
            yield from refs(value)
    elif isinstance(node, str) and node.startswith('#/'):
        yield node


def closure(doc, roots):
    """Finite content closure; self/reciprocal content links are allowed."""
    seen, pending = set(), list(roots)
    while pending:
        ref = pending.pop()
        if ref in seen:
            continue
        seen.add(ref)
        node = resolve(doc, ref)
        if isinstance(node, dict):
            pending.extend(node.get('requires', []))
    return seen


def validate_graph(doc):
    for ref in refs(doc):
        resolve(doc, ref)
    closure(doc, doc['bootstrap']['requires'])
    active, done = set(), set()
    def visit(ref):
        require(ref not in active, 'Procedure invocation cycle: ' + ref)
        if ref in done:
            return
        require(ref.startswith('#/procedures/'), 'Call must target a procedure')
        node = resolve(doc, ref)
        active.add(ref)
        for callee in node['calls']:
            visit(callee)
        active.remove(ref)
        done.add(ref)
    for name in doc['procedures']:
        visit('#/procedures/' + name)
    ids = [v['id'] for v in doc['rules'].values()] + [v['id'] for v in doc['procedures'].values()]
    require(len(ids) == len(set(ids)), 'Duplicate instruction ID')
    require(len(doc['owners']) == 12, 'Twelve logical owners required')
    require({k.split('.')[0] for k in doc['owners']} == {'Aoideon', 'Meleteon', 'Mnemeon'}, 'Plane mismatch')


def render(doc):
    """Readable projection includes every runtime value in a deterministic layout."""
    lines = ['# Helikon Mini Operating', '',
             'Generated from the canonical JSON. Do not edit this projection.', '',
             'The JSON is the selected runtime source for this candidate. This rendering is a reading aid.', '']
    def section(key, value, depth=2):
        if isinstance(value, dict):
            lines.extend(['#' * min(depth, 6) + ' ' + key, ''])
            for k, v in value.items():
                section(k, v, depth + 1)
        elif isinstance(value, list):
            lines.extend(['**' + key + '**', ''])
            if not value:
                lines.extend(['`[]`', ''])
            for item in value:
                if isinstance(item, (dict, list)):
                    lines.extend(['```json', json.dumps(item, ensure_ascii=False, indent=2), '```', ''])
                else:
                    lines.append('- ' + str(item))
            lines.append('')
        else:
            literal = json.dumps(value, ensure_ascii=False) if not isinstance(value, str) else value
            lines.extend(['**' + key + ':** ' + literal, ''])
    for key, value in doc.items():
        section(key, value)
    return '\n'.join(lines).rstrip() + '\n'


def validate_runtime(doc, schema, anchors, system_bytes):
    validate_schema(doc, schema)
    validate_graph(doc)
    for ref, expected in anchors['anchors'].items():
        require(sha(canonical(resolve(doc, ref))) == expected, 'Reviewed policy changed: ' + ref)
    require(sha(system_bytes) == anchors['system_sha256'], 'Reviewed System changed')
    require(len(system_bytes.decode()) <= anchors['budgets']['system_characters'], 'System exceeds design budget')


def validate_repo(root=ROOT):
    root = Path(root)
    doc = load(root / RUNTIME)
    anchor = load(root / 'tests/static/reviewed-contract.json')
    validate_runtime(doc, load(root / SCHEMA), anchor, (root / SYSTEM).read_bytes())
    require(len((root / RUNTIME).read_text()) <= anchor['budgets']['runtime_characters'], 'Runtime exceeds design budget')
    require((root / PROJECTION).read_text() == render(doc), 'Stale generated projection; run render')
    provenance = load(root / 'docs/source-manifest.json')
    for path, expected in provenance['legacy_root_sha256'].items():
        require(sha((root / path).read_bytes()) == expected, 'Legacy bytes changed: ' + path)
    profile = load(root / 'profiles/chatgpt/profiles.json')
    require(profile['identity'] == doc['identity'], 'Profile identity mismatch')
    require({p['id'] for p in profile['profiles']} == {'chatgpt-session','chatgpt-project'} and len(profile['profiles']) == 2, 'Profile inventory mismatch')
    require(all(p['support'] == 'experimental_unverified' for p in profile['profiles']), 'Live support promotion needs a new reviewed gate')
    require(all(p['persistence_claim'] is False and p['delivery'].strip() and p['requires'] for p in profile['profiles']), 'Profile delivery contract invalid')
    require(profile['installation_safeguards'] == {
        'preserve_existing_settings':True,'resolve_unknown_writes_before_retry':True,
        'isolate_from_active_full_helikon':True,'no_bulk_memory_deletion':True,
        'mutations_need_specific_scope':True}, 'Installation safeguards changed')
    require(all(type(v) is bool for v in profile['installation_safeguards'].values()), 'Safeguards must be Boolean')
    mapping = load(root / 'docs/source-to-mini-map.json')
    require(mapping['source_sha256'] == provenance['source']['sha256'], 'Source map provenance mismatch')
    require(mapping['inventory_complete'] is True, 'Source inventory incomplete')
    paths = [r['source_pointer'] for r in mapping['entries']]
    require(len(paths) == len(set(paths)), 'Duplicate source map entry')
    index = load(root / 'docs/source-index.json')
    require(set(paths) == set(index['pointers']), 'Unmapped source component')
    for row in mapping['entries']:
        require(row['disposition'] in {'retain','simplify','exclude'}, 'Invalid source disposition')
        require(bool(row['reason'].strip()), 'Missing mapping rationale')
        require(row['tests'] and set(row['tests']) <= set(load(root / 'tests/behavior/cases.json')['cases']), 'Unresolved case mapping')
        for target in row['targets']:
            resolve(doc, target)
        require(row['disposition'] == 'exclude' or bool(row['targets']), 'Retained source has no destination')
    new_paths = [RUNTIME, SYSTEM, SCHEMA, PROJECTION, Path('README.md'), Path('CHANGELOG.md')]
    new_paths += [p.relative_to(root) for directory in ('docs','profiles','tests/behavior') for p in (root/directory).rglob('*') if p.is_file()]
    private = re.compile(r'libfile[_-]|file_[0-9a-f]{32}|/workspace/|/root/|-----BEGIN .*PRIVATE KEY-----')
    for path in new_paths:
        require(not private.search((root/path).read_text()), 'Private/default account residue: ' + str(path))
    return {'status':'pass','scope':'static_candidate_artifacts_only',
            'runtime_characters':len((root/RUNTIME).read_text()),
            'system_characters':len((root/SYSTEM).read_text()),
            'owners':len(doc['owners']),'source_components':len(paths),
            'live_behavior':'not_run','host_installation':'not_run'}


PAYLOAD = {
 'START_HERE.md':'docs/install.md', 'Helikon_Mini_System.md':str(SYSTEM),
 'Helikon_Mini_Operating_Master.json':str(RUNTIME),
 'Helikon_Mini_Operating.md':str(PROJECTION),
 'Helikon_Mini_Operating_Master.schema.json':str(SCHEMA),
 'MIGRATION.md':'docs/migration.md','RECOVERY.md':'docs/recovery.md',
 'SUPPORT.md':'docs/support-matrix.md','ARCHITECTURE.md':'docs/architecture.md',
 'CHANGELOG.md':'CHANGELOG.md','LICENSE':'LICENSE',
 'SOURCE_MANIFEST.json':'docs/source-manifest.json',
 'PILOT.md':'tests/behavior/README.md','cases.json':'tests/behavior/cases.json',
 'utility.json':'tests/behavior/utility.json'
}


def build(out, root=ROOT):
    root, out = Path(root), Path(out)
    validate_repo(root)
    files = {name:(root / path).read_bytes() for name,path in PAYLOAD.items()}
    manifest = {'format':'helikon-mini.candidate-manifest@1.0.0',
                'identity':load(root / RUNTIME)['identity'],
                'status':'experimental_candidate_live_tests_not_run',
                'members':{name:{'sha256':sha(data),'bytes':len(data)} for name,data in sorted(files.items())}}
    files['MANIFEST.json'] = (json.dumps(manifest, indent=2, ensure_ascii=False)+'\n').encode()
    out.mkdir(parents=True, exist_ok=True)
    target = out / 'Helikon-Mini-4.0.0-candidate.1.zip'
    with zipfile.ZipFile(target, 'w', compression=zipfile.ZIP_STORED) as archive:
        for name,data in sorted(files.items()):
            info = zipfile.ZipInfo(name, date_time=(1980,1,1,0,0,0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    verify_archive(target, files)
    checksum = sha(target.read_bytes())
    (out / (target.name+'.sha256')).write_text(checksum+'  '+target.name+'\n')
    return {'status':'pass','artifact':str(target),'sha256':checksum,'bytes':target.stat().st_size,'members':len(files),'live_support':'unverified'}


def verify_archive(path, expected_files=None):
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        require(len(names) == len(set(names)), 'Duplicate archive member')
        require(set(names) == set(PAYLOAD) | {'MANIFEST.json'}, 'Archive inventory mismatch')
        manifest = strict_json(archive.read('MANIFEST.json').decode())
        require(set(manifest['members']) == set(PAYLOAD), 'Manifest inventory mismatch')
        for name in PAYLOAD:
            data = archive.read(name)
            require(manifest['members'][name] == {'sha256':sha(data),'bytes':len(data)}, 'Member integrity mismatch: ' + name)
        if expected_files is not None:
            require(all(archive.read(n) == data for n,data in expected_files.items()), 'Archive source mismatch')
    return {'status':'pass','scope':'archive_inventory_and_integrity_only'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('render')
    sub.add_parser('validate')
    pack = sub.add_parser('build'); pack.add_argument('--out', default=str(ROOT/'build'))
    verify = sub.add_parser('verify-archive'); verify.add_argument('archive')
    args = parser.parse_args()
    try:
        if args.command == 'render':
            path=ROOT/PROJECTION; path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(render(load(ROOT/RUNTIME)), encoding='utf-8')
            result={'status':'generated','path':str(PROJECTION)}
        elif args.command == 'validate': result=validate_repo()
        elif args.command == 'build': result=build(args.out)
        else: result=verify_archive(args.archive)
        print(json.dumps(result, indent=2))
    except (Invalid, OSError, ValueError, KeyError, TypeError, zipfile.BadZipFile) as exc:
        print(json.dumps({'status':'fail','error':str(exc)})); return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
