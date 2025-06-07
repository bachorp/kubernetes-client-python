#!/bin/bash

# Copyright 2015 The Kubernetes Authors.
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

# Script to fetch latest swagger spec.
# Puts the updated spec at api/swagger-spec/

set -o errexit
set -o nounset
set -o pipefail

# The openapi-generator version used by this client
export OPENAPI_GENERATOR_COMMIT="v4.3.0"
export OPENAPI_GENERATOR_USER_ORG="bachorp"
export OPENAPI_GENERATOR_COMMIT="d4ca25d810422df59423dcc722304b1e278e83db"

SCRIPT_ROOT=$(dirname "${BASH_SOURCE}")
GEN_ROOT="${SCRIPT_ROOT}/../gen"
CLIENT_ROOT="${SCRIPT_ROOT}/../kubernetes"
DOC_ROOT="${SCRIPT_ROOT}/../doc"
CLIENT_VERSION=$(python3 "${SCRIPT_ROOT}/constants.py" CLIENT_VERSION)
PACKAGE_NAME=$(python3 "${SCRIPT_ROOT}/constants.py" PACKAGE_NAME)
DEVELOPMENT_STATUS=$(python3 "${SCRIPT_ROOT}/constants.py" DEVELOPMENT_STATUS)

pushd "${SCRIPT_ROOT}" > /dev/null
SCRIPT_ROOT=`pwd`
popd > /dev/null

source ${SCRIPT_ROOT}/util/common.sh
# util::common::check_sed

pushd "${CLIENT_ROOT}" > /dev/null
CLIENT_ROOT=`pwd`
popd > /dev/null

TEMP_FOLDER=$(mktemp -d)
trap "rm -rf ${TEMP_FOLDER}" EXIT SIGINT

SETTING_FILE="${TEMP_FOLDER}/settings"
echo "export KUBERNETES_BRANCH=\"$(python3 ${SCRIPT_ROOT}/constants.py KUBERNETES_BRANCH)\"" > $SETTING_FILE
echo "export CLIENT_VERSION=\"$(python3 ${SCRIPT_ROOT}/constants.py CLIENT_VERSION)\"" >> $SETTING_FILE
echo "export PACKAGE_NAME=\"client\"" >> $SETTING_FILE

if [[ -z ${GEN_ROOT:-} ]]; then
    GEN_ROOT="${TEMP_FOLDER}/gen"
    echo ">>> Cloning gen repo"
    git clone --recursive https://github.com/kubernetes-client/gen.git "${GEN_ROOT}"
else
    echo ">>> Reusing gen repo at ${GEN_ROOT}"
fi

echo ">>> Running python generator from the gen repo"
"${GEN_ROOT}/openapi/python.sh" "${CLIENT_ROOT}" "${SETTING_FILE}"
mv "${CLIENT_ROOT}/swagger.json" "${SCRIPT_ROOT}/swagger.json"

echo ">>> updating version information..."
gsed -i'' "s/^CLIENT_VERSION = .*/CLIENT_VERSION = \\\"${CLIENT_VERSION}\\\"/" "${SCRIPT_ROOT}/../setup.py"
gsed -i'' "s/^__version__ = .*/__version__ = \\\"${CLIENT_VERSION}\\\"/" "${CLIENT_ROOT}/__init__.py"
gsed -i'' "s/^PACKAGE_NAME = .*/PACKAGE_NAME = \\\"${PACKAGE_NAME}\\\"/" "${SCRIPT_ROOT}/../setup.py"
gsed -i'' "s,^DEVELOPMENT_STATUS = .*,DEVELOPMENT_STATUS = \\\"${DEVELOPMENT_STATUS}\\\"," "${SCRIPT_ROOT}/../setup.py"

docker compose run build-docs

# echo ">>> generating docs..."
# pushd "${DOC_ROOT}" > /dev/null
# make rst
# git add -A .
# popd > /dev/null

echo ">>> Done."
