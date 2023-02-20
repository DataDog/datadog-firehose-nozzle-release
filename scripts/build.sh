#!/usr/bin/env bash

set -euxo pipefail

bosh create-release --force --final --tarball=datadog-firehose-nozzle-release.tgz --version "$VERSION"
