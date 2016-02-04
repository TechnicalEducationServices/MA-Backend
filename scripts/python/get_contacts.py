
import requests
r = requests.get("http://localhost:8080/ETAPP-REST-1/contacts/")
print r.status_code
print r.json()

