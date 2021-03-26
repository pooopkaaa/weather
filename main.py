import requests

places = ['san francisco', 'Лондон', 'svo', 'Череповец']
payload = {'nTqu': '', 'lang': 'en'}
url_template = 'http://wttr.in/{}'

for place in places:
    url = url_template.format(place)
    response = requests.get(url, params=payload)
    response.raise_for_status()
    print(response.text)