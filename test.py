import requests
import json
from collections import OrderedDict
import pprint

url = 'https://nearnoah.net/api/showUserData.json?username=221sdvx'

response = requests.get(url)

# print(response.text)

d = json.loads(response.text)

# 曲データだけ取り出し
trackdata = d['profile']['tracks']

pprint.pprint(trackdata, width=40)