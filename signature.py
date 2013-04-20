import hmac
import time
from hashlib import sha1
from base64 import b64encode, b64decode

#'!run', 'time:1366428313.33', 'ls -lah', 'signature:4d4096ac8a38c6091e4b56c01939677cbd473c55']
#!run|time:1366428282.07|ls -lah|signature:55197a67533b961065dee9a45953ca5602760f6f

def generate_sig(msg,salt):

	signature = hmac.new(salt,msg,sha1).hexdigest()
	command = msg + '|signature:'+signature
	return command 


def validate_sig(msg,salt):

	rslt = command_sig.split('|')
	sig_time = rslt[1].split(':')[1]
	sig_cmd  	= rslt[2]
	sig 		= rslt[3].split(':')[1]
	now = time.time()
	time_diff = abs(float(sig_time) - now)
	if time_diff <  5.00 :
		command = rslt[0]+'|'+rslt[1] + '|'+rslt[2] 
		print command
		gen_signature = hmac.new(salt,command,sha1).hexdigest()
		print gen_signature
		if gen_signature == sig:
			return True
		else:
			return False
		


salt = 'g0ZbaaX1SHzAjlqlGh3E1'
command = '!run|time:'+str(time.time())+'|'+'ls -lah'
command_sig = generate_sig(command,salt)
print command_sig


if validate_sig(command_sig,salt):
	print "Valid"
else:
	print "Not Valid"
#parse1 = command_sig.split('|')
#print parse1
#parse2 = parse1[1].split(':')
#print parse2
#sig_time = parse2[1]
#print sig_time

