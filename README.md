# Basstok storage

Your Account's data should stay understandable and within reach.

Each Account has its own data boundary. Media keeps its ordinary file formats. Structured records use self-describing BEVE v2 in
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

An Account Manager can check an eligible S3 bucket from Data and storage.
The check leaves current storage in use. Explicit confirmation starts the move.

Basstok moves the selected Account's data to the connected bucket. Activity pauses
during the move. You can close the screen and return to check progress. If
access fails, restore the enrolled connection before resuming the same move.

[Customer-managed S3](docs/customer-managed-s3.md) covers bucket requirements
and responsibilities. [Privacy and recovery](docs/privacy-and-recovery.md)
explains what ownership and exported copies do—and do not—provide.

[Explore Basstok](https://basstok.com/)
· [REST API](https://github.com/basstok/api)
· [Contact](mailto:mail@basstok.com)
