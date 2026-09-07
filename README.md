# Basstok storage

Your community's data should stay understandable and within reach.

Basstok keeps community records in readable JSON and media in ordinary
file formats. Community operators can arrange read/export access, inspect the
data with standard tools, and keep their own copies.

## Start with your data

Read a downloaded record with ordinary tools:

```sh
zstd -dc downloaded-record.json.zst | jq .
```

[Your data](docs/your-data.md) explains the formats and how to arrange access.
Use Basstok to make changes; editing stored objects directly is not supported.
Keep exports private, because they can include private community records.

## Use your own bucket

Managers can check bucket settings from Administration on iPhone, Android or
the web. The check leaves your current storage unchanged.

<img src="assets/iphone-storage.png" width="300" alt="Check bucket settings from Basstok on iPhone">

Connecting a customer-managed S3-compatible bucket currently uses assisted
setup. [Contact Basstok](mailto:mail@basstok.com?subject=Customer-managed%20storage)
to check the chosen service and arrange initial setup. The in-app check does
not connect the bucket or move an existing community.

[Customer-managed S3](docs/customer-managed-s3.md) covers bucket requirements
and responsibilities. [Privacy and recovery](docs/privacy-and-recovery.md)
explains what ownership and exported copies do—and do not—provide.

[Explore Basstok](https://basstok.com/) · [Data and control](https://basstok.com/#section-11)
· [REST API](https://github.com/basstok/api) · [Agents](https://github.com/basstok/agents)
· [Contact](mailto:mail@basstok.com)
