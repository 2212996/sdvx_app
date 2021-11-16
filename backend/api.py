import requests
import json
from collections import OrderedDict
import pprint
import random

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
        # レベル→ランプ→グレードの順で絞り込み


# def compare_scores():

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

a = receive_from_API("221sdvx")
pprint.pprint(organize_json(a))