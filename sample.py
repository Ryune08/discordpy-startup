import requests

url = 'https://compass.gamerch.com/UR'

get_url_info = requests.get(url)

print(get_url_info.text)
