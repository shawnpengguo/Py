import requests
import os

# anti 反爬虫

headers = {
    'cookie': 'BIDUPSID=A9BCC19BBD92EE878F22B7AD608A5AD1; PSTM=1731596290; newlogin=1; BAIDUID=A9BCC19BBD92EE870D57994815BCFED6:SL=0:NR=10:FG=1; BDUSS=NFUlBZVk40Q0F1YkF-S2FJWnpLUzVwWEJXb3NReGVObFN-N1JtSThMYklxM0puSVFBQUFBJCQAAAAAAQAAAAEAAAD2bJ2I2qPA79Gwy~vHp7DZtsgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMgeS2fIHktnbm; BDUSS_BFESS=NFUlBZVk40Q0F1YkF-S2FJWnpLUzVwWEJXb3NReGVObFN-N1JtSThMYklxM0puSVFBQUFBJCQAAAAAAQAAAAEAAAD2bJ2I2qPA79Gwy~vHp7DZtsgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMgeS2fIHktnbm; BAIDUID_BFESS=A9BCC19BBD92EE870D57994815BCFED6:SL=0:NR=10:FG=1; ZFY=IZ8eC09M7uYS:Bgdyf0:A75jU3mCBxirsTbQR8nzfK5UA:C; RT="z=1&dm=baidu.com&si=5f05d4de-c557-4352-929a-90ce94ef3fbd&ss=m457pbm0&sl=e&tt=13e2&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1wcfs&ul=219e3&hd=219ek"; H_WISE_SIDS_BFESS=60276_61027_61097_61178_61216_61206_61212_61208_61215_61242_61187_61281_61297; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=60276_61027_61097_61178_61216_61206_61212_61208_61215_61242_61187_61281_61297_60851; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BA_HECTOR=ah2l0485812g0k0101202ga49ubmot1jku57i1u; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; H_WISE_SIDS=61187; PSINO=5; delPer=0; userFrom=www.baidu.com; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; ab_sr=1.0.1_OTQwM2ZkNWZiNGEwYTE5MDkzNjE0MDNlNWIyODMxZTgzYjVjODI0ZDgyNWNjMTRlZWNjYzlkNGQyYjJhOGI3MGQ5NzQyMjhhN2NjYjVjMjBhYjI2YzVmOTI4ODI2YmEwOWZiODNjOTYzNTcyMTUyZjlmOGM5N2U2ZDkzNTQ5YzMyNGVlMmE4ZDc2NGRkNWFkM2E1NDhmZjkwY2UxNTExMw==',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'referer': 'https://image.baidu.com/',
    'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8'
}

pic_url = 'https://image.baidu.com/search/acjson'

common_params = {
    'tn': 'resultjson_com',
    'word': 'python',
    'queryWord': 'python',
}


def get_dynamic_params(pn, rn = 30):
    return {
        'pn': str(pn),
        'rn': str(rn),
    }

def req(url, params = None):
    res = requests.get(url, headers=headers, params=params)
    return res

def download_pic(title, url):
    if not os.path.exists("./pic"):
        os.mkdir("./pic")

    with open(f"./pic/{title}.png", "wb") as f:
        f.write(req(url).content)

def main():
    page_num = 30
    for count in range(2):
        params = get_dynamic_params(str(page_num), 30) | common_params
        page_num += 30
        res = req(pic_url, params=params).json()['data']
        for pic_item in res:
            if  pic_item:
                title = pic_item['fromPageTitle']
                url = pic_item['thumbURL']
                download_pic(title, url)



if __name__ == '__main__':
    main()