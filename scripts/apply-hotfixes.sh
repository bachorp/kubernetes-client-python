#!/bin/sh

# Copyright 2020 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Script to apply hotfixes after generating the client
# More details: https://github.com/kubernetes-client/python/blob/master/devel/release.md#hot-issues

# Check if working directory is dirty
if [ $(git status --porcelain | wc -l) -gt 0 ]
then
    echo Your working directory is not clean. Please clean your working directory.
    exit 1
fi

SCRIPT_ROOT=$(dirname "${BASH_SOURCE}")

# Patching custom client behavior https://github.com/kubernetes-client/python/issues/866
git apply "$SCRIPT_ROOT/custom_objects_api.diff"
if [ $? -eq 0 ]
then
    echo Successfully patched changes for custom client behavior
else
    echo Failed to patch changes for custom client behavior
    exit 1
fi

# Patching commits for enabling from kubernetes import apis
# UPDATE: The commit being cherry-picked is updated to include both the commits as one
# Ref: https://github.com/kubernetes-client/python/blob/0976d59d6ff206f2f428cabc7a6b7b1144843b2a/kubernetes/client/apis/__init__.py
git cherry-pick -n 56ab983036bcb5c78eee91483c1e610da69216d1
if [ $? -eq 0 ]
then
    echo Successfully patched changes for enabling from kubernetes import apis
else
    echo Failed to patch changes for enabling from kubernetes import apis
    git restore --staged .
    exit 1
fi;

echo "Adding custom tests"
mkdir -p "$SCRIPT_ROOT/../kubernetes/client/test"
cp "$SCRIPT_ROOT/test_api_client" "$SCRIPT_ROOT/../kubernetes/client/test/test_api_client.py"


git commit -m "Apply hotfixes"
