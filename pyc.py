import requests
import json
url = "https://api.covid19api.com/live/country/india/status/confirmed"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
