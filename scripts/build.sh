#!/bin/sh
set -eux

./scripts/update-client.sh

rm -r kubernetes/test/
git add .
git commit -m "temporary generated commit"
scripts/apply-hotfixes.sh
git reset HEAD~2
