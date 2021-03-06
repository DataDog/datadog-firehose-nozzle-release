# Datadog Firehose Nozzle Release

This is a BOSH release for the datadog-firehose-nozzle, which transports metrics
from [Loggregator](https://github.com/cloudfoundry/loggregator) to [Datadog](https://www.datadoghq.com/).

## Development

This repository contains only the packaging pieces for the [datadog-firehose-nozzle](https://github.com/DataDog/datadog-firehose-nozzle) to be deployed with [Cloud Foundry BOSH](https://github.com/cloudfoundry/bosh).

See [here](https://bosh.io/docs/create-release/) for more information about the structure of a BOSH release.

The source code is added in the release as a git submobule, and contributions to it must be made on the [datadog-firehose-nozzle repositories](https://github.com/DataDog/datadog-firehose-nozzle).

## Building the Nozzle

From the root of the repository, run:
```bash
VERSION=<YOUR_VERSION> scripts/create-release.sh
```
This will create a BOSH release of the nozzle, with the version you specified. The `datadog-firehose-nozzle-release.tgz` archive of the release is created at the root of the repository.
You can upload this release on your CF environment to make it available and deploy it.

## Deploying the Nozzle

For a general guide to deploying nozzles, see [here](https://docs.cloudfoundry.org/loggregator/nozzle-tutorial.html).

This nozzle assumes you have a Cloud Foundry deployed with a UAA client for
the datadog nozzle. Configuration for the UAA client should look something
like the following.

```
uaa:
  clients:
    datadog-firehose-nozzle:
      access-token-validity: 1209600
      authorities: logs.admin,cloud_controller.admin_read_only,openid,oauth.approvals
      authorized-grant-types: client_credentials,refresh_token
      override: true
      scope: logs.admin,cloud_controller.admin_read_only,oauth.login
      secret: datadog-password
```

Once a Datadog client is registered in UAA, you are ready to deploy the
nozzle. The instructions here assume you are using the Ruby based Bosh CLI and have this deployed on Bosh Lite.

### If you are using Bosh Lite

First, update `bosh-lite/stub.yml` with your Datadog API key.  Note that the
`client_secret` under the `uaa` section in `properties` will need to match
whatever password you set for the UAA client above.

Once the `stub.yml` reflects all the correct credentials, generate a manifest
with:

```
./scripts/make_manifest_spiff bosh-lite/stub.yml
```

### If you are not using Bosh Lite

If you are not usin Bosh Lite, your deployment will require more customization. If you look at the current templates, you'll get a good sense of what you'll need to do in order to deploy the firehose.

For an example manifest, check out `./manifests/examples/example_manifest.yml`

You are now ready to deploy:

```
bosh deploy
```
