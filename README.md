# Basstok storage

Your Account's data should stay understandable and within reach.

Each personal Account or community has its own data boundary. Media keeps its
ordinary file formats. Structured records use self-describing BEVE v2 in
Basstok-managed storage and readable JSON in customer-owned buckets, with
standard Zstandard compression. Authorized owners can arrange read/export access
and keep their own copies.

## Start with your data

For a downloaded record from a customer-owned bucket:

```sh
zstd -dc downloaded-record.json.zst | jq .
```

[Your data](docs/your-data.md) explains the formats and how to arrange access.
Use Basstok to make changes; editing stored objects directly is not supported.
Keep exports private, because they can include private messages and attachments.

## Use your own bucket

Check your bucket from Administration on iPhone, Android or the web. Nothing
moves until an Admin explicitly confirms the storage transfer.

Basstok moves the selected Account's data to the connected bucket. Activity pauses
during the move; you can leave the screen and return to check progress. If a
connection is interrupted, restore access and resume without starting over.

[Customer-managed S3](docs/customer-managed-s3.md) covers bucket requirements
and responsibilities. [Privacy and recovery](docs/privacy-and-recovery.md)
explains what ownership and exported copies do—and do not—provide.

[Explore Basstok](https://basstok.com/)
· [REST API](https://github.com/basstok/api) · [Import](https://github.com/basstok/import)
· [Contact](mailto:mail@basstok.com)
