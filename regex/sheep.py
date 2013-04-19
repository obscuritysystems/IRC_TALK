import re

string1 = 'Sheep 123213'
string2 = 'Sh33p123123'
string3 = 'asdfasdfasdf5h33pasdfasdf'
string4 = 'nota asdfasdf'
string5 = '2312313sheeeeeeeeeeeeeeeep'
string6 = '00123123SH333333333333333P'
string7 = 'shep'
string8 = 'shp'
string9 = 'shpshpshp'
sheep_regex = '.*[sS$5]+[hH(|-|)]+[eE3]+[pP]+.*'

def test (string,regex):

	result = re.search(regex, string)
	if result:
		print 'yes :' + string
		#print 'result'
		regex_array = re.findall(regex,string)
		print 'result :' + regex_array[0]
	else:
		print 'no :' + string



test(string1,sheep_regex)
test(string2,sheep_regex)
test(string3,sheep_regex)
test(string4,sheep_regex)
test(string5,sheep_regex)
test(string6,sheep_regex)
test(string7,sheep_regex)
test(string8,sheep_regex)
test(string9,sheep_regex)



