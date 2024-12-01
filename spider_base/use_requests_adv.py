import requests

# session = requests.Session()
#
# session.headers = {
#     "common": "spg"
# }
#
# res1 = session.get("https://httpbin.org/headers", headers={"common": "myself"})
# res2 = session.get("https://httpbin.org/headers ")
#
# print(res1.text, res2.text)


# url = 'https://httpbin.org/post'
# multiple_files = [
#     ('images', ('test.jpg', open('test.jpg', 'rb'), 'image/jpg'))
#
# ]
# r = requests.post(url, files=multiple_files)
#
# print(r.text)


proxies = {
  'http': 'http://24.115.120.39:8888',
  'https': 'http://24.115.120.39:8888',
}

html = requests.get('https://www.github.com', proxies=proxies)
print(html.text)