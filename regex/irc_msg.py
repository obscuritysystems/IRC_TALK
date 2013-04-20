import re

string1 = ':wright.freenode.net NOTICE * :*** Looking up your hostname...'
string2 = ':wright.freenode.net 255 NemusBot2 :I have 3666 clients and 1 servers'
string3 = 'asdfasdfasdf5h33pasdfasdf'

regex = '^(:(\S+) )?(\S+)( (?!:)(.+?))?( :(.+))?$'

matchObj = re.match(regex, string2, re.M|re.I)

if matchObj:
   print "FULL : ", matchObj.group()
   print "Prefix: ", matchObj.group(1)
   print "matchObj.group(2): ", matchObj.group(2)
   print "Command : ", matchObj.group(3)
   print "matchObj.group(4): ", matchObj.group(4)
   print "matchObj.group(5): ", matchObj.group(5)
   print "Tail: ", matchObj.group(6)
else:
   print "No match!!"
