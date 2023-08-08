import socket
import requests
import pprint
import json
from colorama import init



print('\n=============== Welcome to mobile legend ==================')
print('================== Create By Manwhide =====================')
hostname = input("\n[+] Enter a domain name : ")
print('\n')
ip_address = socket.gethostbyname(hostname)

request_url = 'https://geolocation-db.com/jsonp/' + ip_address
response = requests.get(request_url)
geolocation = response.content.decode()
geolocation = geolocation.split("(")[1].strip(")")
geolocation = json.loads(geolocation)
for k,v in geolocation.items():
	pprint.pprint(str(k) + ' : ' + str(v))

print('\n======================== WIN!! ============================')

