import urllib

import requests

# HTTP eskaerak 4 atal ditu: metodoa, uria, goiburuak eta edukia
#Las comillas simples y las dobles son lo mismo en python

metodoa = 'POST'

#Uria ez da https://ws-sendingformdata.appspot.com/html/form.html aldiz uria jakiteko "ver codigo fuente" -> "action"
#atalean begiratu
uria = "http://ws-sendingformdata.appspot.com/processForm"


goiburuak = {'Host': 'ws-sendingformdata.appspot.com',
             'Content-Type': 'application/x-www-form-urlencoded'}

edukia = {'nan': '78989898'}

#baina datuak nan = 79879898 formatuan bidali egin behar dira horretarako mezua parseatu egin behar dugu
edukia_encoded = urllib.parse.urlencode(edukia)
goiburuak['Content-Length'] = str(len(edukia_encoded))

erantzuna = requests.request(metodoa, uria, data=edukia, headers=goiburuak, allow_redirects=False)
kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(str(kodea) + " " + deskribapena)

edukia = erantzuna.content
print(edukia)
