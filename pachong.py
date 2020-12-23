import json

import requests

url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
word = input("输入地址：")
data = {
    "cname": "",
    "pid": "",
    "keyword": word,
    "pageIndex": "1",
    "pageSize": "10"
}
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 "
                  "Safari/537.36 "
}

response = requests.post(url=url, data=data, headers=headers)

page_test = json.loads(response.text)

infoPage = page_test["Table1"]

test_len = len(infoPage)
print(test_len)
for i in range(0, test_len - 1):
    print("--------------------------------")
    print("排名：", infoPage[i]['rownum'])
    print("商店名称：", infoPage[i]['storeName'])
    print("省份：", infoPage[i]['provinceName'])
    print("所在城市：", infoPage[i]['cityName'])
    print("详细地址：：", infoPage[i]['addressDetail'])
    print("提供额外服务：", infoPage[i]['pro'])
    print("--------------------------------")

kdj = word + ".html"
with open(kdj, "w", encoding="utf-8") as fp:
    fp.write(response.text)
    fp.close()
print("over!")
