import requests

PLACES = ['Лондон', 'svo', 'Череповец']
PAYLOAD = {'n': '', 'T': '', 'q': '', 'c': '', 'm': '', 'M': '', 'lang': 'ru'}


def main():
    url_template = 'http://wttr.in/{}'

    for place in PLACES:
        url = url_template.format(place)
        response = requests.get(url, params=PAYLOAD)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
