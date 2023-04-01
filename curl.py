import requests
from requests.structures import CaseInsensitiveDict
#from urllib2 import Request, urlopen
import json
import pandas as pd  


url = "https://einfo.ceproas.cz/cepro_portal_ws/rest/common/prox/mobileData"

headers = CaseInsensitiveDict()
headers["accept-encoding"] = "gzip"
headers["authorization"] = "Basic bW9iYXA6RVdpa0Ey"
headers["connection"] = "Keep-Alive"
headers["content-length"] = "99"
headers["content-type"] = "application/json; charset=UTF-8"
headers["host"] = "einfo.ceproas.cz"
headers["user-agent"] = "okhttp/4.9.0"

data = '{  "search": {    "exclude_cs_ceny": false,   "exclude_cs_kvalita": false  },  "version": 5}'


resp = requests.post(url, headers=headers, data=data)

json_object = json.dumps(resp.text)


print(json_object)
print(resp.status_code)
