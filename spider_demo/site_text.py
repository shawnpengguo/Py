import requests
from bs4 import BeautifulSoup

text_url = 'https://www.txt123.net/tt/8015/'

headers = {
    'cookie': 'Hm_lvt_fdcd1040ed481616f6e938076eaf8171=1733233768; HMACCOUNT=06F5F26E415E5746; Hm_lpvt_fdcd1040ed481616f6e938076eaf8171=1733234693',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

session = requests.Session()
session.headers.update(headers)

def req(url, path):
    res = session.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    format_data = soup.select(path)
    return format_data

def main():
    all_title_link = req(text_url, '#list dl dd a')
    for link in all_title_link:
        cur_link = 'https:' + link.get('href')
        cur_content = req(cur_link, '.content_read #content')
        for text in cur_content:
            print(link.text ,text.text)



if __name__ == '__main__':
    main()