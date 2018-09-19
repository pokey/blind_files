#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

SECTION=minor
[[ $# -eq 1 && $1 == "--patch" ]] && SECTION=patch

NEW_VERSION=$(bumpversion --dry-run --list $SECTION | \
                 grep new_version | sed -r s,"^.*=",,)
git flow release start v$NEW_VERSION
bumpversion $SECTION
git flow release publish
git flow release finish
git checkout master
git push origin master --tags
git checkout develop
git push origin develop --tags
