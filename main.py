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

# resp = requests.head("http://www.httpwatch.com/httpgallery/chunked/chunkedimage.aspx")
# print(resp.status_code)


erantzuna = requests.request(metodoa, uria, timeout=2.50)

# Orain erantzunetik datuak aterako ditugu
# HTTP erantzunak 4 atal ditu: kodea, deskribapena, goiburuak eta edukia

kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(str(kodea) + " " + deskribapena)
for goiburua in erantzuna.headers:
    print(goiburua + ": " + erantzuna.headers[goiburua])
edukia = erantzuna.content
print(edukia)

fitxategia = open("irudia.jpg", 'wb')
fitxategia.write(edukia)
fitxategia.close()
