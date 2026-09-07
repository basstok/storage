# Customer-managed S3

Customer-managed storage places a community's durable data in a dedicated
private bucket under the customer's storage account. The data format and
community permissions stay the same.

Open **Administration → Data and storage** on iPhone, Android or the web.
Enter your bucket settings and choose **Check bucket**. Basstok tests access
using temporary data, then removes it. Your current storage is unchanged.

When you are ready, choose **Move community**. This separate confirmation moves
an existing Basstok-managed community to your bucket. Community activity pauses
while its data moves. You can close the screen and return to check progress;
an interrupted move resumes after access is restored. Unfinished uploads may
need to be started again. Completed files and community permissions remain
intact.

## What a target needs

- A dedicated, empty, private bucket.
- A TLS-verified HTTPS endpoint and signing region.
- A separate service credential restricted to the bucket operations Basstok needs.
- S3 object reads, byte ranges, writes, conditional creation and deletion.
- Bucket access checks and object listing.
- Multipart upload, part listing, completion, cancellation and signed part uploads.
- For browser uploads, CORS permission for the community's exact origin and required upload requests.

“S3-compatible” alone does not establish compatibility. The full upload,
recording, permission and recovery behavior must be verified for the selected
provider before production use. A successful object upload is not enough.

## Responsibilities

The customer controls the storage account, billing, availability, public-access
policy and provider-level permissions. Keep the bucket private. Give human
inspectors read/export access separately from Basstok's service credential.

**Upload cleanup:** Basstok attempts to cancel failed uploads. Interrupted
uploads can leave incomplete parts that incur storage charges. Configure your
provider to remove incomplete multipart uploads, for example after seven days,
or clean them up with its own tools. Do not expire completed community data.
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
