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
"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
response = requests.post(url=url,data=data,headers=headers)

page_test = response.text
kdj = word+".html"
with open(kdj,"w",encoding="utf-8") as fp:
    fp.write(page_test)
print("over!")