from fontTools.ttLib import TTFont
import requests
from bs4 import BeautifulSoup

sxs_url = "https://www.shixiseng.com/interns?keyword=python&city=%E5%85%A8%E5%9B%BD&type=intern"
sxs_font_url = "https://www.shixiseng.com/interns/iconfonts/file?rand=0.11867541871369092"

headers = {
    'cookie': 'utm_source_first=PC; adClose=true; __jsluid_s=4a8444ec2323636618424b102b6cb5b7; Hm_lvt_03465902f492a43ee3eb3543d81eba55=1733409933; HMACCOUNT=06F5F26E415E5746; adCloseOpen=true; utm_source=hd-pc-wzl-hj; utm_campaign=hd-hjsx25; position=pc_search_syss; bottom_banner=true; Hm_lpvt_03465902f492a43ee3eb3543d81eba55=1733410219',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
}

def parse_and_write_font():
    res = requests.get(url=sxs_font_url, headers=headers)
    with open('font', 'wb') as f:
        f.write(res.content)
    font = TTFont('./font')
    font.saveXML('font.xml')
    cmap = font['cmap'].getBestCmap()
    new_dict = {}
    for k, v in cmap.items():
        if v == 'x':
            continue
        v = v.replace('uni', '')
        if len(v) < 4:
            v = ("\\u00" + v).encode('utf-8').decode('unicode-escape')
            new_dict[hex(k)] = v
        else:
            v = ("\\u" + v).encode('utf-8').decode('unicode-escape')
            new_dict[hex(k)] = v
    return new_dict

def req_site():
    res = requests.get(url=sxs_url, headers=headers).text
    soup = BeautifulSoup(res, 'lxml')
    res_div = soup.select('.f-l .intern-detail__job')
    new_dict = parse_and_write_font()
    for div in res_div:
        cur_title = div.select_one('p').select_one('a')['title'].replace('&#', '0')
        for k,v in new_dict.items():
            title = cur_title.replace(k,v)
            print(k,v,title)
            # todo 这段有问题没有找到key，排查中～


req_site()

