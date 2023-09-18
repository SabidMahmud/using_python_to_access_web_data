import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


print(f"=====Accessing Json Files and Extracting data=====")
address = input("Enter address: ")
print(f"Accessing {address}")

ulopen = urllib.request.urlopen(address)
print("=== Reading Data ===")

data = ulopen.read()
print(f"Retrieved {len(data)} elements..")
info = json.loads(data)

comments = info['comments']
# print( comments )
sum = 0
for i in comments:
    # print(i['count'])
    sum += i["count"]

print(f"Sum = {sum}")
