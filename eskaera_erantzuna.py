"""
Programa honek webgune batean gordetako irudi bat jeitsi
eta fitxategi batean gordetzen du.
Irudia jeisteko, HTTP prokoloa erabiliko dugu.
"""

import requests

# HTTP eskaerak 4 atal ditu: metodoa, uria, goiburuak eta edukia
metodoa = 'GET'
uria = 'http://www.httpwatch.com/httpgallery/chunked/chunkedimage.aspx'
goiburuak = {'Host ': 'www.httpwatch.com'}
edukia = ''


erantzuna = requests.request(metodoa, uria, data=edukia, allow_redirects=False)

# Orain erantzunetik datuak aterako ditugu
# HTTP erantzunak 4 atal ditu: kodea, deskribapena, goiburuak eta edukia

kodea = erantzuna.status_code
deskribapena = erantzuna.reason

print(str(kodea) + " " + deskribapena)
for goiburua in erantzuna.headers:
    print(goiburua + ": " + erantzuna.headers[goiburua])
edukia = erantzuna.content
print(edukia)

fitxategia = open("irudia.jpg", 'wb') #Write binary
fitxategia.write(edukia)
fitxategia.close()
