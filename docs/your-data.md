# Your data

A Basstok community has a dedicated Object Storage data boundary. Its durable
records include Content, Comments, Members, Chats, Messages, Labels and Asset
metadata. Files and recordings keep their ordinary media formats.

## Readable records

Structured records are readable JSON, compressed with standard Zstandard in
files ending in `.json.zst`. You do not need Basstok software to inspect a
downloaded record:

```sh
zstd -dc downloaded-record.json.zst | jq .
```

Records may contain related information together. Do not assume that every
Comment or Message is a separate file.

Storage exports can contain private information. Inspect them only on trusted
devices, and restrict access to downloaded copies as carefully as the original.

## Access and copies

For Basstok-managed storage, contact [Basstok](mailto:mail@basstok.com) to arrange
appropriate read/export access. This is separate from a Member's access inside
the community: a storage export can include information that an ordinary Member
cannot read through the app.

Use your storage provider's normal tools to retrieve records and media. Keep
copies together and protected. Downloading readable data is not the same as
automatically converting it into another product's format.

## Make changes through Basstok

Use the apps or an appropriately authorized Basstok REST API client to change
community data. Editing, replacing or deleting stored objects directly is not
a supported way to update a community, change permissions or repair records.

[Privacy and recovery](privacy-and-recovery.md) · [Back to storage](../README.md)
