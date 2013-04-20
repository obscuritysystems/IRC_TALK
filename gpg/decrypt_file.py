import gnupg

gpg = gnupg.GPG(gnupghome='/home/testgpguser/gpghome')
with open('my-encrypted.txt.gpg', 'rb') as f:
    status = gpg.decrypt_file(f, passphrase='my passphrase', output='my-decrypted.txt')

	print 'ok: ', status.ok
	print 'status: ', status.status
	print 'stderr: ', status.stderr


