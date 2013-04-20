import gnupg

gpg = gnupg.GPG(gnupghome='/home/testgpguser/gpghome')
open('my-unencrypted.txt', 'w').write('You need to Google Venn diagram.')
with open('my-unencrypted.txt', 'rb') as f:
    status = gpg.encrypt_file(
        f, recipients=['testgpguser@mydomain.com'],
        output='my-encrypted.txt.gpg')

print 'ok: ', status.ok
print 'status: ', status.status
print 'stderr: ', status.stderr


