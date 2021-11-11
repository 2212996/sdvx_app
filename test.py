import requests
import json
from collections import OrderedDict
import pprint

username = '221sdvx'
url = 'https://nearnoah.net/api/showUserData.json?username=' + username

response = requests.get(url)

d = json.loads(response.text)

# 曲データだけ取り出し
trackdata = d['profile']['tracks']

# 任意の難易度の楽曲を取り出す

#　難易度の変数
difficulty = 19

# 難易度の名前一覧の配列
diff_rank = ['novice', 'advanced', 'exhaust', 'infinite', 'gravity', 'heavenly', 'vivid', 'maximum']

scorebox = []
for i in range(len(trackdata)):
    tmp = trackdata[i]
    for j in range(len(diff_rank)):
        if(diff_rank[j] in tmp):
            tmp_dif = tmp[diff_rank[j]]
            scorebox_cell = []
            if('score' in tmp_dif and tmp[diff_rank[j]]['level'] == difficulty):
                scorebox_cell.append(tmp['title'])
                scorebox_cell.append(tmp[diff_rank[j]]['score'])
                scorebox.append(scorebox_cell)
                # print(tmp['title'] + ' : ' + str(tmp[diff_rank[j]]['score']))

print(scorebox)
# 綺麗な形式でjsonを出してくれるやつ
# pprint.pprint(trackdata, width=40)