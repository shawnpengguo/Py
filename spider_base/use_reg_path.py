import re
import requests

myTitle = re.compile('"excerptArea":{"text":(.*?)"},"imageArea', re.I | re.S | re.M)
myUrl = re.compile('"url":"(.*?)"}', re.I | re.S | re.M)

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

url = 'https://www.zhihu.com/billboard'

html = requests.get(url, headers=headers)

title = myTitle.findall(html.text)
urls = myUrl.findall(html.text)
for i,j in zip(title,urls):
    url = str(j).replace(r"\u002F", '/')
    print('标题：{}, 链接：{}'.format(i,url ))
# print(title, urls)