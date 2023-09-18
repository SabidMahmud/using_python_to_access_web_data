import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

place = input("Enter Location: ")
param = {}
param['address'] = place
if api_key is not False: 
    param['key'] = api_key

url = urllib.parse.urlencode(param)
target_url = serviceurl + url
# print(target_url)

print(f"Retriving {target_url}")

connect = urllib.request.urlopen(target_url, context=ctx)
data = connect.read().decode()

print(f"Retrived {len(data)} elements.")

try:
    js = json.loads(data)
except:
    js = None

if not js:
    print('==== Failure To Retrieve ====')
    print(data)

# print(json.dumps(js, indent=4))
print(f"Place Id: {js['results'][0]['place_id']}")
