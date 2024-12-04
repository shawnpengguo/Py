import re
import httpx

# ts m3u8
# 旧案例也有了加密 后续学到补上

m_common_url = 'https://www.olevod.com'
m_detail_play_url = "/player/vod/1-41175-1.html"

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
    'referer': 'https://www.olevod.com/'
}

session = httpx.Client()
session.headers.update(headers)





def main():
    pass


if __name__ == '__main__':
    main()