import httpx
from bs4 import BeautifulSoup

common_url = "https://cn.proxy-tools.com/proxy/cn"

headers = {
    'cookie': 'cf_clearance=.htli7sP6VsdBMJ7wkD9S4kZDTwnQLWNEdao7oyHcEg-1733408568-1.2.1.1-prZ5ja.XLimndhGh8Wfg7RXmC4DESO8zggCDDdeu8qQ_UqiAGGpVQGk.2CQ1Fjr8WE.h_52.IKm5UDT9mHb5Vc5Iiv2p9ygqGA.kzggI8uH2F6dnRJkDy60RVnAD4lF9CDIjj.WzriaN7hUcqAfc8XBW.Z.Vp88WxYW78DEtpJfudyvQ4TBCWsGsx6kyAVEE_c3KQF8oYTTMdHc3WlmsbsoTacA9EYDF94Mh2IpSgGxDP1G3gqR7bFt.vMpwAWAp0G1VlNj7Z7RiueOdLeVigucnf17JxkInWmUHxf8k1hGrB0WJK7vGDReUl9h6Ztgo4vr9B4V92MwcDeDP3lrAgZ_xqvFgUa.38Lwdn7UE6ucuQR2SCmDDK2HmjUMS5dhXiaJaX_k6U.Xk8eyufKEZXZ93lQFoqqyXlL1sR5TQukp37fc4TlwMZE_XcXvPa45.; _gid=GA1.2.1543759813.1733408602; _gat_gtag_UA_194946253_1=1; _ym_uid=1733408603656778556; _ym_d=1733408603; _ym_isad=2; _ga_627B8J0D01=GS1.1.1733408601.1.1.1733408607.0.0.0; _ga=GA1.1.1570011715.1733408602; _ga_NK4CCQ342Z=GS1.1.1733408601.1.1.1733408607.0.0.0; XSRF-TOKEN=eyJpdiI6IkZKTTNRbW5OY2JuV1ZWVVE0MmRXc2c9PSIsInZhbHVlIjoiL2Q2RDE3TnF6cW1hZzdobTRzcC90bWxubi9iQXE1V3UxOWhMUk1zU2FiaFZybThLV0hhaUt4c2JiSWVZODh5VEQ2Z1BqT0hnVnV4Y2VaNmF6RHFvRjl3MGpCb2NUaTYxOGVOdjdjVTNOcnI3SDhFSXNrTXNpdmZ3ZEU1aVpaUFciLCJtYWMiOiI0YjU2NWI1OWI4OTM1YTBiYzgyNDYwZDRkZGM3YTVjMjQ0ZjA2OTNhZDk5YTQ1MWU3M2U4OWQyMzBiZjdkMzJjIiwidGFnIjoiIn0%3D; proxy_toolscom_session=eyJpdiI6IjVGYzE4YnFjRU1sT3k0SThNai8yaUE9PSIsInZhbHVlIjoiVDJqa1RVVEhES3d1NmIvTjBLYjYxMEF2ZWhjV1c0SGlJS0hIUjZ2N0FPRGQwYnJtVjNUei9pa2tUbk5RQ2dlSXIzbm50MEpQUHNsMFk1Nnl5eEhsT09zajl1N0hFdnNxNnFRTEpka2RlMzh1UC94Rk5NTFlGNlBXakJRYVRtMG8iLCJtYWMiOiI3NDJlOTY3ZGNhYzA0MzI3MGZjODUxZDgxOWZjYmY1MWIxMDhjOGQ5Njk0YTY0MWI3ZjkzMmVlMTVkNzhlYmQzIiwidGFnIjoiIn0%3D',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-',
}

session = httpx.Client()
session.headers.update(headers)

def req(url):
    res = session.get(url)
    return res

def format_res(res, tag):
    soup = BeautifulSoup(res.text, 'lxml')
    soup_res = soup.select(tag)
    res_list = []
    for ip in soup_res:
        res_list.append(ip.text)
    return res_list

def main():
    req_res = req(common_url)
    res = format_res(req_res, '.table tr>td:first-child')
    # 端口图片加密 后续 todo 
    print(res)


if __name__ == '__main__':
    main()