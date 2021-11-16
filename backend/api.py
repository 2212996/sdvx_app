import requests
import json
from collections import OrderedDict
import pprint
import random

def save_from_API(username):

    url = 'https://nearnoah.net/api/showUserData.json?username=' + username
    response = requests.get(url)
    rawdata = json.loads(response.text)

    with open(username + '_score.json', 'w') as f:
        json.dump(rawdata, f, ensure_ascii=False)

def open_json(username):
    with open(username + '_score.json', 'rb') as fin:
        d = json.load(fin)
    return d

# 任意のユーザーのスコアリストをAPIのから取得する
def receive_from_API(username):

    url = 'https://nearnoah.net/api/showUserData.json?username=' + username
    response = requests.get(url)
    rawdata = json.loads(response.text)

    return rawdata

# jsonデータをパースする
def organize_json(rawdata):

    # 曲データだけ取り出し
    trackdata = rawdata['profile']['tracks']

    # 全ての曲データが入る配列
    scorebox = [] 

    # 難易度の名前一覧の配列
    diff_rank = ['novice', 'advanced', 'exhaust', 'infinite', 'gravity', 'heavenly', 'vivid', 'maximum']

    for i in range(len(trackdata)):

        #　一曲分のデータを格納
        tmp_song = trackdata[i]

        #　タイトル,idを格納
        tmp_title = tmp_song['title']
        tmp_id = tmp_song['id']

        # １曲を難易度ごとに分解して整理
        for j in range(len(diff_rank)):
            if(diff_rank[j] in tmp_song):

                # 譜面ごとにデータ整理
                tmp_chart = tmp_song[diff_rank[j]]

                # 未プレイの場合の処理
                if('clearlamp' not in tmp_chart):
                    organized_data = {'id': tmp_id,
                        'title': tmp_title,
                        'level': tmp_chart['level'], 
                        'difficulty': diff_rank[j], 
                        'clearlamp': 'NOPLAY', 
                        'grade': 'F', 
                        'score': 0
                        }
                    scorebox.append(organized_data)

                # スコアデータの格納
                else:
                    organized_data = {'id': tmp_id,
                        'title': tmp_title,
                        'level': tmp_chart['level'], 
                        'difficulty': diff_rank[j], 
                        'clearlamp': tmp_chart['clearlamp'], 
                        'grade': tmp_chart['grade'], 
                        'score': tmp_chart['score']
                        }
                    scorebox.append(organized_data)

    return scorebox

def to_narrowdown_songs(scorebox, minlevel, maxlevel, clearlamp, grade):

    # clearlampの絞り込みが無かった場合、全てにチェックを付ける
    if(len(clearlamp) == 0):
        clearlamp = ['NOPLAY', 'CRASH', 'COMP', 'EX COMP', 'UC', 'PER']

    # gradeの絞り込みが無かった場合、全てにチェックを付ける
    if(len(grade) == 0):
        grade = ['F', 'D', 'C', 'A', 'A+', 'AA', 'AA+', 'AAA', 'AAA+', 'S', '995', '998']

    # 絞り込み
    for i in range(len(scorebox))[::-1]:
        tmp_scorebox = scorebox[i]
        if(
            not(tmp_scorebox['level'] >= minlevel and tmp_scorebox['level'] <= maxlevel)
            or not(tmp_scorebox['clearlamp'] in clearlamp)
            or not(tmp_scorebox['grade'] in grade)
            ):
            del scorebox[i]

    return scorebox

def make_id_list(scorebox):

    id_list = set()

    for i in range(len(scorebox)):
        tmp_scorebox = scorebox[i]
        id_list.add(tmp_scorebox['id'])

    return id_list

def to_narrowdown_byID(scorebox, id_list):

    narrowed_scorebox = []
    a = 0
    for i in range(len(scorebox)):
        tmp_scorebox = scorebox[i]
        if(tmp_scorebox['id'] == id_list[a]):
            narrowed_scorebox.append(tmp_scorebox)
            a = a + 1

    return narrowed_scorebox

def cals_scoregap(scorebox1, scorebox2):

    id_1 = []
    id_2 = []

    id_1 = make_id_list(scorebox1)
    id_2 = make_id_list(scorebox2)

    id_intersection = id_1 & id_2

    id_listed = list(id_intersection)

    scorebox1 = to_narrowdown_byID(scorebox1, id_listed)
    scorebox2 = to_narrowdown_byID(scorebox2, id_listed)

    scoregap = []
    for i in range(len(scorebox1)):
        user1_song = scorebox1[i]
        user2_song = scorebox2[i]
        diff = user1_song['score'] - user2_song['score']

        scoregap.append({'title': user1_song['title'], 'gap': diff})

    return scoregap

def to_narrowdown_byGap(scoregap, gap):
    for i in range(len(scoregap)):
        

# 以下、テストケース

# test = [{'advanced': {'clearlamp': 'UC',
#                     'grade': 'S',
#                     'level': 12,
#                     'score': 9986864,
#                     'volforce': 23},
#         'exhaust': {'clearlamp': 'COMP',
#                     'grade': 'S',
#                     'level': 15,
#                     'score': 9954562,
#                     'volforce': 17
#         },
#         'id': 1608,
#         'maximum': {'clearlamp': 'EX COMP',
#                     'grade': 'S',
#                     'level': 18,
#                     'score': 9905564,
#                     'volforce': 38},
#         'novice': {'clearlamp': 'PUC',
#                     'grade': 'S',
#                     'level': 5,
#                     'score': 9999592,
#                     'volforce': 8},
#         'title': 'Destr0yer'}]

# a = receive_from_API("221sdvx")

a221 = open_json('221sdvx')
b221 = organize_json(a221)
adas = open_json('ddr_das')
bdas = organize_json(adas)

minlevel = 18
maxlevel = 18
clearlamp = []
grade = []

c221 = to_narrowdown_songs(b221, minlevel, maxlevel, clearlamp, grade)
cdas = to_narrowdown_songs(bdas, minlevel, maxlevel, clearlamp, grade)

d = cals_scoregap(c221, cdas)

print(d)