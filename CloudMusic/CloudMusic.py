import json
import os
import re

import requests
from lxml import etree

url = "https://music.163.com/discover/toplist"  # 网易云每日飙升榜
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
content = requests.get(url)
data = etree.HTML(content.text)
result = data.xpath('//ul[@class="f-hide"]/li/a/text()')
# data = etree.HTML(content.text)
textarea = data.xpath('//textarea[@id="song-list-pre-data"]/text()')
# data.xpath("//*")

# with open("result.json","w",encoding="utf-8") as re:
#     re.write(textarea[0])
#     pass
CurrentPath = os.getcwd()
file_dir = os.path.join(CurrentPath, "Music")
data_dir = os.path.join(CurrentPath, "Data")
if os.path.exists(file_dir):
    pass
else:
    os.mkdir(file_dir)

if os.path.exists(data_dir):
    pass
else:
    os.mkdir(data_dir)

songInfo = json.loads(textarea[0])
count = 1
succ = 0
f = 0
for value in songInfo:
    print("排名：", count)
    print("歌曲名：", value['name'])
    print("演唱：", value['artists'][0]['name'])
    print(value['id'])
    count = count + 1
    new_name = re.sub(r'[/\:?*"<>|]+', '_', value['name'])
    artName = re.sub(r'[/\:?*"<>|]+', '_', value['artists'][0]['name'])
    file_path = r"{}/{} - {}.mp3".format(file_dir, artName, new_name)
    music_base = "http://music.163.com/song/media/outer/url?id={}".format(value['id'])

    with open(file_path, "wb") as mu:
        try:
            req = requests.get(music_base, headers=headers)
            mu.write(req.content)
            print("下载 {}.mp3 成功".format(new_name))
            succ = succ + 1
            print()
        except Exception as e:
            p = print("读取 {}.mp3 失败".format(new_name))
            f = f + 1
            continue

print("成功下载：", succ)
print("失败：", f)
