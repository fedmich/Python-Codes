#Python 2
import urllib
response = urllib2.urlopen("http://python.org/")
content = response.read()

#Python 3
import urllib.request
url = urllib.request.urlopen("http://www.python.org")
content = url.read()
print ( content )