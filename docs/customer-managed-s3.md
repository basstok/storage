# Customer-managed S3

Customer-managed storage places the selected Account's durable data in a
dedicated private bucket under the customer's storage account. Structured
records are readable JSON and retain their identities and permissions. Each
Account has its own data boundary.

Open **Administration → Data and storage** where available. The current
Account Manager can choose **Check bucket** to test credentials, object access
and multipart operations with temporary data. Basstok removes the probes and
leaves the current storage selection in use.

When you are ready, explicitly confirm the move. This separate confirmation moves
the existing Account data to your bucket. Ordinary activity pauses during
the move. Check progress after reopening the app or after a service restart.
If access fails, restore it and resume with the same enrolled connection.
Unfinished uploads may need to be started again.

## What a target needs

- A dedicated, empty, private bucket.
- A public HTTPS endpoint with a trusted certificate and a signing region.
- A separate service credential restricted to the bucket operations Basstok needs.
- S3 object reads, byte ranges, writes, conditional creation and deletion.
- Bucket access checks and object listing.
- Multipart upload, part listing, completion, cancellation and signed part uploads.
- For browser uploads, CORS permission for the community's exact origin and required upload requests.

“S3-compatible” alone does not establish compatibility. The full upload,
recording, permission and recovery behavior must be verified for the selected
provider before production use. Verify browser CORS separately where browser
uploads are needed. The bucket check leaves provider lifecycle and CORS rules
unchanged.

## Responsibilities

The customer controls the storage account, billing, availability, public-access
policy and provider-level permissions. Keep the bucket private. Give human
inspectors read/export access separately from Basstok's service credential.

**Upload cleanup:** Basstok attempts to cancel failed uploads. Interrupted
uploads can leave incomplete parts that incur storage charges. Configure your
provider to remove incomplete multipart uploads, for example after seven days,
or clean them up with its own tools. Keep completed Account data outside the
incomplete-part cleanup rule.
Basstok does not read or change your lifecycle rules, and lifecycle API support
is not required.

Basstok uses the enrolled target for supported community changes. It does not
create or replace a customer's bucket implicitly. Credential rotation must be
verified before the old credential is revoked; revoking the active credential
can interrupt service. Replacing an already connected customer bucket is not
part of the in-app move. Contact Basstok before changing that target.

Do not post credentials, private bucket addresses or data exports in GitHub
issues or email. Enter connection credentials only in the authorized storage
screen, or arrange a secure setup with Basstok.

[Privacy and recovery](privacy-and-recovery.md) · [Back to storage](../README.md)
