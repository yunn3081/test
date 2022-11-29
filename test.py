from kkbox_developer_sdk.auth_flow import KKBOXOAuth
import requests
import json
import time
from datetime import datetime

# KKBOX華語新歌日榜
url = "https://kma.kkbox.com/charts/api/v1/daily?category=297&lang=tc&limit=50&terr=tw&type=newrelease"
# 取得歌曲資訊json檔
response = requests.get(url)
# 將json字串轉為Python的字典型態
data = json.loads(response.text)

song_list = data["data"]["charts"]["newrelease"]
my_dict={}

# 取得每首歌的排名、曲名、連結、作者、時間
for song in song_list:
    song_rank = song["rankings"]["this_period"]
    song_name = song["song_name"]
    song_url = song["song_url"]
    song_artist = song["artist_name"]
    song_timestamp = int(song["release_date"])
    # 從timestamp轉為日期格式
    song_date = time.strftime(
        "%Y-%m-%d", time.localtime(song_timestamp))

    musicdetail = {'song_rank': song_rank, 'song':song_name, 'singer':song_artist, 'release_date':song_date}
    my_dict[song_name] = musicdetail


data = my_dict
# print(data)
for item in data.items():
    ranking = item[1]['song_rank']
    song = item[1]['song']
    singer = item[1]['singer']
    release_date = item[1]['release_date']

    # print(song_rank, song, singer, release_date)
    print(song_name)

# print(my_dict)