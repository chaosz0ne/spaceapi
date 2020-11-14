import requests


with open('status.json.in') as st_in:
	content = st_in.read()

obj = requests.get("http://api.open-notify.org/iss-now.json").json()

lat = obj['iss_position']['latitude']
lon = obj['iss_position']['longitude']

with open('status.json', 'w') as st_out:
	st_out.write(content % (lat, lon))