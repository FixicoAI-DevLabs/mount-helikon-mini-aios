#!/usr/bin/env python3
"""Publish only the explicitly approved, immutable candidate-5 package.

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
import urllib.request

import mini

ROOT = Path(__file__).resolve().parents[1]
REPO = 'FixicoAI-DevLabs/mount-helikon-mini-aios'
TAG = 'v4.0.0-candidate.5'
TARGET = '733a9d5ff2a7eda17e4adc8cddd7cacada6a0f12'
TARGET_TREE = '61bac510d20626c05305c70cc6acec1cba4ca216'
TITLE = 'Helikon Mini 4 — Project beta (candidate 5)'
DIRECTORY = ROOT / 'release/4.0.0-candidate.5'
ZIP = DIRECTORY / 'Helikon-Mini-4.0.0-candidate.5.zip'
CHECKSUM = DIRECTORY / (ZIP.name + '.sha256')
NOTES = DIRECTORY / 'RELEASE_NOTES.md'
ZIP_SHA = 'd4fcf46e86ba349906ce5ade1572502adbdfeec1849ff19f62b2372b0176653a'
EXPECTED_FILES = {
    ZIP: ZIP_SHA,
    ROOT / 'src/runtime/Helikon_Mini_Operating_Master.json':
        '21f2635f72b3e519d4d25041ef968d2b121df4e8bfb5552a0cc595374c02e378',
    ROOT / 'src/system/Helikon_Mini_System.md':
        'f8432f2f677cca9c95d4a813e4609586eed067e545ff397fcc5b99de56d5ea3f',
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
    require(ZIP.stat().st_size == 98043, 'ZIP size changed')
    require(CHECKSUM.read_text() == f'{ZIP_SHA}  {ZIP.name}\n', 'Checksum file changed')
    mini.verify_archive(ZIP)
    require(NOTES.is_file(), 'Prepared release notes missing')
    return {'status': 'pass', 'scope': 'offline_frozen_package',
            'tag': TAG, 'target': TARGET, 'zip_sha256': ZIP_SHA}


def check_release(release):
    require(release['tag_name'] == TAG, 'Unexpected release tag')
    require(release['target_commitish'] == TARGET, 'Unexpected release target')
    require(release['prerelease'] is True, 'Release is not classified as prerelease')
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
    require(os.environ.get('GITHUB_REF') == 'refs/heads/release/mini-project-beta',
            'Wrong publication branch')
    require(bool(os.environ.get('GH_TOKEN')), 'Runner token unavailable')
    check_package()
    require(api('git/commits/' + TARGET)['tree']['sha'] == TARGET_TREE,
            'Approved commit tree differs')

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
           '--prerelease', '--latest=false')
        release = find_release()
        require(release is not None, 'Draft release not observed after create')
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
           '--prerelease', '--latest=false')
    release = find_release()
    check_release(release)
    require(release['draft'] is False, 'Release publication not observed')
    check_tag()

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
               'assets': downloads,
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
