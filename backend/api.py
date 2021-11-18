import requests
import json
import pprint
import random
from collections import OrderedDict

# 任意のユーザー名のスコアデータをAPIから取得する関数
def save_from_API(username):

    try:
        url = 'https://nearnoah.net/api/showUserData.json?username=' + username
        response = requests.get(url)
        rawdata = json.loads(response.text)

        with open(username + '_score.json', 'w') as f:
            json.dump(rawdata, f, ensure_ascii=False)

    except requests.exceptions.RequestException as e:
        print("エラー",e)

# ローカルに保存しているjsonファイルを開く関数
def open_json(username):

    try:
        with open(username + '_score.json', 'rb') as fin:
            d = json.load(fin)

        # 返り値はdsonデータ
        return d

    # FileNotFoundErrorは例外クラス名
    except FileNotFoundError as e: 
        print("ファイルが見つかりません", e)

# 任意のユーザーのスコアリストをAPIのから取得する
def receive_from_API(username):

    try:
        url = 'https://nearnoah.net/api/showUserData.json?username=' + username
        response = requests.get(url)
        rawdata = json.loads(response.text)

        # 返り値はjsonデータ
        return rawdata

    except requests.exceptions.RequestException as e:
        print("エラー",e)

# jsonデータをパースする
def organize_json(rawdata):

    # ユーザー名が正しくなくてjsonの中身が
    # {"errormsg": "ユーザデータが見つかりません。"}
    # となっている場合のエラー処理
    if ("errormsg" in rawdata):
        print("ユーザー名が正しくありません")

    else:
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
                    # タイトル、レベル、難易度は埋める
                    # それ以外は
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

        # 返り値は配列
        return scorebox

# 絞り込み条件と一致する曲目だけを返す関数
def to_narrowdown_songs(scorebox, minlevel, maxlevel, clearlamp, grade, difficulty):

    # clearlampの絞り込みが無かった場合、全てにチェックを付ける
    if(len(clearlamp) == 0):
        clearlamp = ['NOPLAY', 'CRASH', 'COMP', 'EX COMP', 'UC', 'PER']

    # gradeの絞り込みが無かった場合、全てにチェックを付ける
    if(len(grade) == 0):
        grade = ['F', 'D', 'C', 'A', 'A+', 'AA', 'AA+', 'AAA', 'AAA+', 'S']

    # difficultyの絞り込みが無かった場合、全てにチェックを付ける
    if(len(difficulty) == 0):
        difficulty = ['novice', 'advanced', 'exhaust', 'infinite', 'gravity', 'heavenly', 'vivid', 'maximum']


    # 条件による絞り込み
    for i in range(len(scorebox))[::-1]:
        tmp_scorebox = scorebox[i]
        if(
            not(tmp_scorebox['level'] >= minlevel and tmp_scorebox['level'] <= maxlevel)
            or not(tmp_scorebox['clearlamp'] in clearlamp)
            or not(tmp_scorebox['grade'] in grade)
            or not(tmp_scorebox['difficulty'] in difficulty)
            ):
            del scorebox[i]

    if (len(scorebox) == 0):
        print('該当する曲がありません5')
        return scorebox

    else:
        # 返り値は配列
        return scorebox

# cals_scoregap関数の処理に用いる
# 曲リストのidのみを抽出した配列
def make_id_list(scorebox):

    # 集合を定義
    id_list = set()

    for i in range(len(scorebox)):
        tmp_scorebox = scorebox[i]
        id_list.add(tmp_scorebox['id'])

    # 返り値は集合
    return id_list

# cals_scoregap関数の処理に用いる
# make_id_list関数で抽出したidのみの曲リストを作成する
def to_narrowdown_byID(scorebox, id_list):

    narrowed_scorebox = []
    a = 0
    for i in range(len(scorebox)):
        tmp_scorebox = scorebox[i]
        if(tmp_scorebox['id'] == id_list[a]):
            narrowed_scorebox.append(tmp_scorebox)
            a = a + 1

    # 返り値は配列
    return narrowed_scorebox

# ２プレイヤーのスコア差を返す関数
def cals_scoregap(scorebox1, scorebox2):

    id_1 = []
    id_2 = []

    id_1 = make_id_list(scorebox1)
    id_2 = make_id_list(scorebox2)

    # 2つの集合の和集合を返す
    id_intersection = id_1 & id_2

    if(len(id_intersection) == 0):
        print('error')
        scoregap = []
        # 返り値は配列
        return scoregap

    else:
        id_listed = list(id_intersection)
        id_listed.sort()

        scorebox1 = to_narrowdown_byID(scorebox1, id_listed)
        scorebox2 = to_narrowdown_byID(scorebox2, id_listed)

        scoregap = []
        # １曲毎の点差を計算する処理
        for i in range(len(scorebox1)):
            user1_song = scorebox1[i]
            user2_song = scorebox2[i]
            diff = user1_song['score'] - user2_song['score']

            scoregap.append({'title': user1_song['title'], 'gap': diff})

        # 返り値は配列
        return scoregap

# 任意の点差範囲を指定して絞り込む
def to_narrowdown_byGap(scoregap, gap):

    applicable_songs = []
    for i in range(len(scoregap)):
        tmp_scoregap = scoregap[i]
        diff = tmp_scoregap['gap']
        if(abs(diff) <= gap):
            applicable_songs.append(tmp_scoregap)

    if(len(applicable_songs) == 0):
        print('該当曲がありません6')
        return applicable_songs

    else:
        # 返り値は配列
        return applicable_songs

# 任意の点差範囲を指定して絞り込む
def to_narrowdown_byGap_revenge(scoregap, gap):

    applicable_songs = []
    for i in range(len(scoregap)):
        tmp_scoregap = scoregap[i]
        diff = tmp_scoregap['gap']
        if(abs(diff) >= gap):
            applicable_songs.append(tmp_scoregap)

    if(len(applicable_songs) == 0):
        print('該当曲がありません7')
        return applicable_songs
        
    else:
        # 返り値は配列
        return applicable_songs

# applicable_songsの中からランダムで1曲を選ぶ関数
def select_song_randomly(applicable_songs):
    value = random.randint(0, len(applicable_songs))

    if(len(applicable_songs) == 0):
        a = []
        print('該当曲がありません8')
        return a
        
    else:
        # 返り値は辞書型
        return applicable_songs[value] 

def output(your_id, opp_id, minlevel, maxlevel, difficulty, clearlamp, grade, scoregap):

    try:
        error = {'title': '該当曲がありません', 'gap': 'うんち'}

        # ローカルに保存しているjsonファイルを開く
        your_json = open_json(your_id)
        opp_json = open_json(opp_id)

        # jsonデータをパース
        your_data = organize_json(your_json)
        opp_data = organize_json(opp_json)

        # 絞り込み条件と一致する曲目だけを返す
        your_songlist = to_narrowdown_songs(your_data, minlevel, maxlevel, clearlamp, grade, difficulty)
        opp_songlist = to_narrowdown_songs(opp_data, minlevel, maxlevel, clearlamp, grade, difficulty)

        if(len(your_songlist) == 0 or len(opp_songlist) == 0):
            return error

        # ２プレイヤーのスコア差を返す
        gap_list = cals_scoregap(your_songlist, opp_songlist)

        if(len(gap_list) == 0):
            return error

        narroweddown = to_narrowdown_byGap(gap_list, scoregap)

        if(len(narroweddown) == 0):
            return error

        # applicable_songsの中からランダムで1曲を選ぶ
        result = select_song_randomly(narroweddown)

        return result

    except NameError:  # 処理する例外の型が指定されている
        print('koko')
        return error
    except IndexError:
        print('kokodayo')
        return error



#
#
#
# 以下、テストケース
#
#
#

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

# a221 = open_json('221sdvx')
# b221 = organize_json(a221)
# adas = open_json('ddr_das')
# bdas = organize_json(adas)

# minlevel = 19
# maxlevel = 19
# clearlamp = []
# grade = []
# difficulty = []

# c221 = to_narrowdown_songs(b221, minlevel, maxlevel, clearlamp, grade, difficulty)
# cdas = to_narrowdown_songs(bdas, minlevel, maxlevel, clearlamp, grade, difficulty)

# d = cals_scoregap(c221, cdas)
# e = to_narrowdown_byGap(d, 10000)
# f = select_song_randomly(e)

# pprint.pprint(f)

test = output('221sdvx', 'ddr_das', 19, 19, [], [], [], 10000)
print(test)

# print(test)

# a = receive_from_API('221sdvx')
# b = organize_json(a)
# c = to_narrowdown_songs(b, 19, 19, ['EX COMP', 'COMP'], ['S'], [])