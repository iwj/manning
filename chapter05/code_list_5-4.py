import urllib2
manning_url = "http://helloworldbook2.com/data/message.txt"
file = urllib2.urlopen(manning_url)
message = file.read()
print message
