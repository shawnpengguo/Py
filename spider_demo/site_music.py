import httpx
from bs4 import BeautifulSoup

headers = {
    'cookie': 'kg_mid=8379e0a6de288f655eb22a348f66e8ee; kg_dfid=34bgVz0iMJkI2Zkn832zEj4q; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1733238288; HMACCOUNT=06F5F26E415E5746; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22gzlogin-user.kugou.com%22%5D%5D%7D; KuGooRandom=66171733238548614; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1733238763',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'referer': 'https://www.kugou.com/'
}

all_songs_url = "https://www.kugou.com/yy/html/rank.html"
sign_song = "https://wwwapi.kugou.com/play/songinfo"

session = httpx.Client(headers=headers, http2=True)

def req(url):
    res = httpx.get(url)
    return res

def format_sign_song_url(eid):
    # to do 解密后续学到再做
    params = {
        'encode_album_audio_id': eid,
        'uuid': '',
        'signature': ''
    }
    res = req(sign_song)

def main():
    res = req(all_songs_url)
    soup = BeautifulSoup(res.text, "lxml")
    song_list = soup.select('#rankWrap .pc_temp_songlist ul li')
    for song in song_list:
        song_title = song.get('title')
        song_eid = song.get('data-eid')
        print(song_title, song_eid)


if __name__ == '__main__':
    main()