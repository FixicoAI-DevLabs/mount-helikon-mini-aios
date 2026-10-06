#!/usr/bin/env python3
"""Publish only the explicitly approved, immutable Mini 4.0.0 package.

--check is offline. --publish requires the dedicated GitHub Actions branch
and its repository-scoped token. Existing conflicting releases/assets stop
the operation; they are never overwritten, deleted or silently adopted.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
import time
import urllib.request

import mini

ROOT = Path(__file__).resolve().parents[1]
REPO = 'FixicoAI-DevLabs/mount-helikon-mini-aios'
TAG = 'v4.0.0'
TARGET = '8c18052b4781514317181d14f4b20790622780e7'
TARGET_TREE = '53adb2d8a7360b368a9ee31e4c52171d16e54acd'
TITLE = 'Helikon Mini 4.0.0 — Helikon 6 rebuild'
DIRECTORY = ROOT / 'release/4.0.0'
ZIP = DIRECTORY / 'Helikon-Mini-4.0.0.zip'
CHECKSUM = DIRECTORY / (ZIP.name + '.sha256')
NOTES = DIRECTORY / 'RELEASE_NOTES.md'
ZIP_SHA = '8e5493e7106f3fe3341f1a47129f0230173804759a77da6d8c92fd949fafe108'
EXPECTED_FILES = {
    NOTES: '86f01aa05343f9abf642a804ad7004cf2bb16a5a0a1b251f262fff1ab516fc5c',
    ZIP: ZIP_SHA,
    ROOT / 'Helikon_Mini_Operating_Master.json':
        'a8b54f99268c8ad8d6639f16820243041e82986ed52f78a6d9c79b0482643700',
    ROOT / 'Helikon_Mini_System.md':
        'd996b9f62e7455587470a0ecea09802bc0c3698b1919a3910f0fe25d70b00d29',
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def gh(*args):
    # Tokens stay in the runner environment; never in arguments or receipts.
    result = subprocess.run(['gh', *args], check=True, capture_output=True,
                            text=True, timeout=90)
    return result.stdout


def api(path):
    return json.loads(gh('api', f'repos/{REPO}/{path}'))


def find_release():
    pages = json.loads(gh('api', '--paginate', '--slurp',
                         f'repos/{REPO}/releases?per_page=100'))
    matches = [r for page in pages for r in page if r['tag_name'] == TAG]
    require(len(matches) <= 1, 'Multiple matching releases')
    return matches[0] if matches else None


def check_package():
    for path, expected in EXPECTED_FILES.items():
        require(digest(path.read_bytes()) == expected, f'Frozen bytes changed: {path.name}')
    require(ZIP.stat().st_size == 96424, 'ZIP size changed')
    require(CHECKSUM.read_text() == f'{ZIP_SHA}  {ZIP.name}\n', 'Checksum file changed')
    mini.verify_archive(ZIP)
    require(NOTES.is_file(), 'Prepared release notes missing')
    return {'status': 'pass', 'scope': 'offline_frozen_package',
            'tag': TAG, 'target': TARGET, 'zip_sha256': ZIP_SHA}


def check_release(release):
    require(release['tag_name'] == TAG, 'Unexpected release tag')
    require(release['target_commitish'] == TARGET, 'Unexpected release target')
    require(release['prerelease'] is False, 'Release must be a regular current release')
    require(release['name'] == TITLE, 'Release title differs from approved title')
    require(release['body'].strip() == NOTES.read_text().strip(), 'Release notes differ')
    names = [a['name'] for a in release['assets']]
    require(len(names) == len(set(names)), 'Duplicate asset names')
    require(set(names) <= {ZIP.name, CHECKSUM.name}, 'Unexpected release assets')


def check_tag():
    value = api(f'git/ref/tags/{TAG}')['object']
    visited = set()
    while value['type'] == 'tag':
        require(value['sha'] not in visited and len(visited) < 5, 'Invalid tag chain')
        visited.add(value['sha'])
        value = api('git/tags/' + value['sha'])['object']
    require(value['type'] == 'commit' and value['sha'] == TARGET,
            'Tag does not resolve to approved merge commit')


def publish():
    require(os.environ.get('GITHUB_ACTIONS') == 'true', 'Publishing requires GitHub Actions')
    require(os.environ.get('GITHUB_REPOSITORY') == REPO, 'Wrong repository')
    require(os.environ.get('GITHUB_REF') == 'refs/heads/release/mini-4.0.0',
            'Wrong publication branch')
    require(bool(os.environ.get('GH_TOKEN')), 'Runner token unavailable')
    check_package()
    require(api('git/commits/' + TARGET)['tree']['sha'] == TARGET_TREE,
            'Approved commit tree differs')

    runs = api('actions/runs?head_sha=' + TARGET)['workflow_runs']
    require(any(r['head_sha'] == TARGET and r['path'] == '.github/workflows/candidate.yml'
                and r['conclusion'] == 'success' for r in runs),
            'Reviewed main commit has no passing Mini CI run')

    # Inspect existing tags before any release mutation. Missing is allowed;
    # a conflicting pre-existing tag cannot be repaired by moving it.
    tag_pages = json.loads(gh('api', '--paginate', '--slurp',
                             f'repos/{REPO}/tags?per_page=100'))
    if any(t['name'] == TAG for page in tag_pages for t in page):
        check_tag()

    release = find_release()
    if release is None:
        gh('release', 'create', TAG, '--repo', REPO, '--target', TARGET,
           '--title', TITLE, '--notes-file', str(NOTES), '--draft',
           '--latest=false')
        for _ in range(6):
            release = find_release()
            if release is not None:
                break
            time.sleep(2)
        require(release is not None, 'Draft release not observed after create; inspect before retry')
    check_release(release)

    # Inspect/read existing assets before retrying uploads; never clobber.
    existing = {a['name']: a for a in release['assets']}
    for path in (ZIP, CHECKSUM):
        if path.name not in existing:
            require(release['draft'], 'Published release is missing an expected asset')
            gh('release', 'upload', TAG, str(path), '--repo', REPO)
        with tempfile.TemporaryDirectory() as destination:
            gh('release', 'download', TAG, '--repo', REPO,
               '--pattern', path.name, '--dir', destination)
            downloaded = (Path(destination) / path.name).read_bytes()
            require(downloaded == path.read_bytes(), f'Uploaded asset differs: {path.name}')

    release = find_release()
    check_release(release)
    require({a['name'] for a in release['assets']} == {ZIP.name, CHECKSUM.name},
            'Draft asset inventory incomplete')
    if release['draft']:
        gh('release', 'edit', TAG, '--repo', REPO, '--draft=false',
           '--prerelease=false', '--latest')
    release = find_release()
    check_release(release)
    require(release['draft'] is False, 'Release publication not observed')
    check_tag()

    latest = None
    for _ in range(6):
        latest = api('releases/latest')
        if latest['id'] == release['id'] and latest['tag_name'] == TAG:
            break
        time.sleep(2)
    require(latest['id'] == release['id'] and latest['tag_name'] == TAG,
            'Latest release does not point to Mini 4.0.0')

    downloads = []
    expected = {ZIP.name: ZIP.read_bytes(), CHECKSUM.name: CHECKSUM.read_bytes()}
    with tempfile.TemporaryDirectory() as destination:
        for asset in release['assets']:
            url = asset['browser_download_url']
            require(url.startswith(f'https://github.com/{REPO}/releases/download/{TAG}/'),
                    'Unexpected public asset URL')
            # Public GET deliberately sends no token or other credentials.
            with urllib.request.urlopen(url, timeout=60) as response:
                body = response.read(len(expected[asset['name']]) + 1)
            require(body == expected[asset['name']], 'Public download differs')
            path = Path(destination) / asset['name']
            path.write_bytes(body)
            if path.suffix == '.zip':
                mini.verify_archive(path)
            downloads.append({'name': asset['name'], 'bytes': len(body),
                              'sha256': digest(body), 'url': url})
    receipt = {'status': 'published_and_public_download_verified',
               'repository': REPO, 'tag': TAG, 'target_commit': TARGET,
               'release_id': release['id'], 'release_url': release['html_url'],
               'prerelease': release['prerelease'], 'published_at': release['published_at'],
               'latest_verified': True, 'assets': downloads,
               'fresh_chatgpt_installation': 'not_evaluated_by_this_workflow'}
    path = ROOT / 'build/release-publication-receipt.json'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--check', action='store_true')
    mode.add_argument('--publish', action='store_true')
    args = parser.parse_args()
    if args.check:
        print(json.dumps(check_package(), indent=2))
    else:
        publish()
