import json
import httpx
from bs4 import BeautifulSoup

yw_first_url = 'https://news.163.com/special/cm_yaowen20200213/?callback=data_callback'

headers = {
    'cookie': '_ntes_origin_from=baidu; _ntes_nuid=2a2866e00c3e0b0a58253db93ea372a8; s_n_f_l_n3=3c1a8314c3211a8c1733325248091; _antanalysis_s_id=1733325248553; BAIDU_SSP_lcr=https://www.baidu.com/link?url=eCqB28KI8WWsa_vvt08Vy7KoGSHxZBOA0h_-m2RF9Ru&wd=&eqid=9569574c00013d7b00000004675071bd; ne_analysis_trace_id=1733325280677; vinfo_n_f_l_n3=3c1a8314c3211a8c.1.1.1733323764113.1733323774933.1733325280747',
    'referer': 'https://news.163.com/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
}

session = httpx.Client()
session.headers.update(headers)

def req(url):
    res = session.get(url)
    return res

def callback_res_reg(res):
    format_res = res.replace('data_callback(', '')
    re = format_res[:len(format_res)-1]
    return re

def format_detail_bs4(detail_res, tag):
    soup = BeautifulSoup(detail_res.text, 'lxml').select(tag)
    return soup

def main():
    res = callback_res_reg(req(yw_first_url).text)
    json_res = json.loads(res)
    for doc in json_res:
        cur_doc_title = doc['title']
        cur_doc_detail_url = doc['docurl']
        cur_doc = req(cur_doc_detail_url)
        format_cur_doc = format_detail_bs4(cur_doc, '.post_body')
        for detail in format_cur_doc:
            if len(detail) > 0:
                print(cur_doc_detail_url, detail.text)


if __name__ == '__main__':
    main()