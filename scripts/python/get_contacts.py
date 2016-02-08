import requests
r = requests.get("http://localhost:8080/ETAPP-REST-1/contacts/")
print r.status_code
print r.json()
#import urllib2

#url = 'http://localhost:8080/ETAPP-REST-1/contacts/'
#response = urllib2.urlopen(url).read()
#print response

