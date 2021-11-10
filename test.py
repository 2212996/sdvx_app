import requests
import json
from collections import OrderedDict
import pprint

url = 'https://nearnoah.net/api/showUserData.json?username=221sdvx'

response = requests.get(url)

d = json.loads(response.text)

# 曲データだけ取り出し
trackdata = d['profile']['tracks']

# 竹の白譜面のスコアを返すテスト
take = trackdata[1710]
take_score = take['maximum']['score']
print(take_score)

# pprint.pprint(trackdata[1710], width=40)