import requests
import json
from collections import OrderedDict
import pprint
import random

def make_scorelist(username, difficulty):
    url = 'https://nearnoah.net/api/showUserData.json?username=' + username

    response = requests.get(url)

    d = json.loads(response.text)

    # 曲データだけ取り出し
    trackdata = d['profile']['tracks']

    # 難易度の名前一覧の配列
    diff_rank = ['novice', 'advanced', 'exhaust', 'infinite', 'gravity', 'heavenly', 'vivid', 'maximum']

    # 全てのスコアと曲名の配列が入ったやつ
    scorebox = []

    # 曲データごとのfor文
    for i in range(len(trackdata)):
        tmp = trackdata[i]

        # 難易度名ごとに探索
        for j in range(len(diff_rank)):
            if(diff_rank[j] in tmp):
                tmp_dif = tmp[diff_rank[j]]
                scorebox_cell = []
                if(tmp[diff_rank[j]]['level'] == difficulty):
                    if('score' in tmp_dif):
                        scorebox_cell.append(tmp['title'])
                        scorebox_cell.append(tmp[diff_rank[j]]['score'])
                        scorebox.append(scorebox_cell)
                    else:
                        scorebox_cell.append(tmp['title'])
                        scorebox_cell.append(0)
                        scorebox.append(scorebox_cell)

    return scorebox

# 2プレイヤーの点差を返す関数
def compare_scores(result_1, result_2):

    # 全ての曲名とスコア差の配列が入ったやつ
    diffbox = []

    if(len(result_1) == len(result_2)):

        for i in range(len(result_1)):
            #　一曲の曲名とスコア差を入れる
            diffbox_cell = []
            result_1_box = result_1[i]
            result_2_box = result_2[i]
            diff = result_1_box[1] - result_2_box[1]
            diffbox_cell.append(result_1_box[0])
            diffbox_cell.append(diff)
            diffbox.append(diffbox_cell)
    else:
        print("正常にスコアを取得出来ませんでした")

    return diffbox

# compare_scoresで作成したリストから任意の点差の曲目を返してくれる関数
def return_applicable_songs(results, desig_diff):

    applicable_songs = []
    # 該当曲が無かった時のエラー処理を考えよう！！！！！！
    for i in range(len(results)):
        results_box = results[i]
        diff = results_box[1]
        if(abs(diff) <= desig_diff):
            applicable_songs.append(results_box)

    return applicable_songs

# applicable_songsの中からランダムで1曲を選ぶ関数
def select_song_randomly(applicable_songs):
    value = random.randint(0, len(applicable_songs))
    return applicable_songs[value]

# ２人分のスコアツールのユーザー名、難易度、点差の４つが必要
result_1 = make_scorelist('221sdvx', 19)
result_2 = make_scorelist('ddr_das', 19)

result = compare_scores(result_1, result_2)
applicable_songs = return_applicable_songs(result, 10000)
song = select_song_randomly(applicable_songs)

print('選ばれた曲は ' + song[0] + ' です！')
print('点差は ' + str(song[1]) + ' です！')