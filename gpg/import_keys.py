import gnupg
from pprint import pprint

gpg = gnupg.GPG(gnupghome='/home/testgpguser/gpghome')
key_data = open('mykeyfile.asc').read()
import_result = gpg.import_keys(key_data)
pprint(import_result.results)
