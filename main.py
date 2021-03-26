import requests

url = 'http://wttr.in/san%20francisco?nTqu&lang=en'
response = requests.get(url)
response.raise_for_status()

print(response.text)