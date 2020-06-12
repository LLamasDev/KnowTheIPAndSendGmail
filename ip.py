import urllib.request
import json
import datetime
from gmail import *

with urllib.request.urlopen('https://geolocation-db.com/json') as url:
    data = json.loads(url.read().decode())
    ip = data['IPv4']

fecha = datetime.date.today()
IPtxt = open('./file/ip.txt','r+')
ultimaLinea = IPtxt.readlines()[-1]
ultimaLinea = ultimaLinea.split(' ')[1]

if ultimaLinea != ip:
    texto = '\n' + str(fecha) + ': ' + str(ip)
    IPtxt.write(texto)
    IPtxt.close()
    email(texto)