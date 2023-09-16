from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

#ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False 
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter Url: ")
count = int(input("Count: "))
position = int(input("Position: "))

names = []

for _ in range(count):
    print(f"Retrieving {url}")
    html = urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    #retrieving the anchor tags
    tags = soup('a')
    name = tags[position - 1].contents[0]
    print([name])
    names += [name]
    url = tags[position - 1]['href']
    
# print(names)
print(names[-1])


