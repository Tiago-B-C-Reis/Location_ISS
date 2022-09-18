import urllib.request
import json


response = urllib.request.urlopen('http://api.open-notify.org/iss-now.json')
print(response)

obj = json.loads(response.read())
lat = obj['iss_position']['latitude']
long = obj['iss_position']['longitude']

url = 'https://www.openstreetmap.org/?mlat=' + str(lat) + '&mlon=' + str(long) + '#map=3/' + str(lat) + '/' + str(long)
import webbrowser
webbrowser.open_new_tab(url)

