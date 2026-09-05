# Privacy and recovery

Storage ownership is a useful control, not a claim that Basstok cannot process
your data.

## Two different kinds of access

Inside Basstok, Members and delegated Agents remain subject to the community's
permissions and the resources they may access. Choosing a different storage
provider does not give an Agent or Member extra permissions.

Provider-level storage access is separate. Someone allowed to export a bucket
may obtain private records as well as public Content. Grant it deliberately,
limit who receives exported copies, and keep public bucket access disabled.

## Changes and integrity

Basstok is the supported way to change community data. In the customer-managed
integration, altered or outdated stored records are rejected rather than
treated as authorized updates. Direct bucket edits can make affected data
unavailable; they are not a repair interface.

Owning the bucket does not make the service zero-knowledge or guarantee that
the bucket is the only place data is processed or retained. Basstok needs to
process data to provide the product. See the [privacy policy](https://basstok.com/privacy)
for how information is handled.

## Copies are not automatic recovery

Keep appropriate backups and protect them from accidental deletion. A readable
copy helps preserve custody, but it does not by itself establish that the copy
contains the latest permissions, revocations or community changes.

Recovery must establish trustworthy current data before access resumes. Do not
restore an arbitrary older export into an active bucket or assume it will be
accepted. Contact [Basstok](mailto:mail@basstok.com) before a recovery or storage
change. Deleting the data bucket can destroy the community's durable data;
customer-managed storage does not include a promise of automatic recovery.

[Your data](your-data.md) · [Back to storage](../README.md)
