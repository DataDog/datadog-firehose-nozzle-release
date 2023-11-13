# Changelog


## 87 / 2023-11-13

* [Added] Upgrade nozzle to 2.7.0. Read more about it [here](https://github.com/DataDog/datadog-firehose-nozzle/releases/tag/2.7.0).
* [Added] Upgrade go to 1.21.3. See [#125](https://github.com/DataDog/datadog-firehose-nozzle-release/pull/125).
* [Added] Add properties for the application logs collection feature. See [#124](https://github.com/DataDog/datadog-firehose-nozzle-release/pull/124).
* [Added] Add scheme prefix handling for the property `nozzle.dca_url`. See [#123](https://github.com/DataDog/datadog-firehose-nozzle-release/pull/123).
* [Added] Make `nozzle.dca_url` and `nozzle.dca_token` properties optional. See [#122](https://github.com/DataDog/datadog-firehose-nozzle-release/pull/122).

## 86 / 2022-11-14

* [Added] Upgrade nozzle to 2.5.0. Read more about it [here](https://github.com/DataDog/datadog-firehose-nozzle/releases/tag/2.5.0).
* [Added] Add option to enable/disable app metadata prefix in app metrics. See [#116](https://github.com/DataDog/datadog-firehose-nozzle-release/pull/116).
* [Fixed] Fix `org_data_collection_interval` property name. See [#117](https://github.com/DataDog/datadog-firehose-nozzle-release/pull/117).

## 85 / 2022-04-25

* [Added] Upgrade nozzle to 2.4.1. Read more about it [here](https://github.com/DataDog/datadog-firehose-nozzle/releases/tag/2.4.1).
* [Added] Add option to enable advanced tagging. See [#113](https://github.com/DataDog/datadog-firehose-nozzle-release/pull/113).
* [Added] Add configuration values for the DCA properties. See [#110](https://github.com/DataDog/datadog-firehose-nozzle-release/pull/110).

## 84 / 2022-04-13

* [Added] Upgrade nozzle to 2.4.0. Read more about it [here](https://github.com/DataDog/datadog-firehose-nozzle/releases/tag/2.4.0).

## 83 / 2021-08-09

* [Fixed] Fix broken 82 release built with outdated go version, resulting in inconsistent vendoring.

## 82 / 2021-08-09

* [Fixed] Support building in air gapped environment. See [#104](https://github.com/DataDog/datadog-firehose-nozzle-release/pull/104).

## 81 / 2021-08-09

* [Added] Upgrade nozzle to 2.3.0. See [#102](https://github.com/DataDog/datadog-firehose-nozzle-release/pull/102).
  - See [Nozzle changelog](https://github.com/DataDog/datadog-firehose-nozzle/blob/master/CHANGELOG.md#230--2021-08-05) for more information.
* [Added] Upgrade go version to 1.16. See [#101](https://github.com/DataDog/datadog-firehose-nozzle-release/pull/101).

## 80 / 2020-07-23

* [Added] Add labels and annotations as tags. See [#99](https://github.com/DataDog/datadog-firehose-nozzle-release/pull/99).
