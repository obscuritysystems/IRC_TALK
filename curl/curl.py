import pycurl
import json
import StringIO

c = pycurl.Curl()
c.setopt(c.URL, 'http://data.mtgox.com/api/2/BTCUSD/money/ticker')
c.setopt(c.CONNECTTIMEOUT, 5)
c.setopt(pycurl.FOLLOWLOCATION, 1)
c.setopt(c.TIMEOUT, 8)
b = StringIO.StringIO()
c.setopt(c.COOKIEFILE, '') 
c.setopt(c.FAILONERROR, True)
c.setopt(c.HTTPHEADER, ['Accept: application/json', 'Content-Type: application/x-www-form-urlencoded'])
c.setopt(pycurl.WRITEFUNCTION, b.write)
try:
	c.perform()
	bitcoin_data = json.loads(b.getvalue())
	print bitcoin_data

except pycurl.error, error:
    errno, errstr = error
    print 'An error occurred: ', errstr
