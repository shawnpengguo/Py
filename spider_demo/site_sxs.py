import os
from fontTools.ttLib import TTFont
import requests
from bs4 import BeautifulSoup

from spider_base.use_reg_path import title

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
    soup_res = []
    for div in res_div:
        soup_res.append(div.select_one('p').select('a')[0].get('title'))
    return soup_res


def main():
    font_res = parse_and_write_font()
    site_res = req_site()
    for res in site_res:
        fm = res.replace('&#', '0')
        for k, v in font_res.items():
            ss = fm.replace(k, v)
            print(ss)

if __name__ == '__main__':
    main()

