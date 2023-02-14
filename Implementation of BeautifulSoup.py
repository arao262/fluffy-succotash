import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = int(input("Enter a count : "))
position = int(input("Enter a position : "))

url = "http://py4e-data.dr-chuck.net/known_by_Patryk.html"

for i in range(count):
    html = urllib.request.urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    tag = tags[position-1].get('href', None)
    print("Retrieving:" , tag)
    url = tag
