import requests
from urllib.parse import quote, unquote

# --------------------post
# wd = quote(input('please input search keywords: '))
#
# params = {
#     'wd': wd
# }
#
# headers = {
# 'cookie': 'BIDUPSID=A9BCC19BBD92EE878F22B7AD608A5AD1; PSTM=1731596290; BD_UPN=123253; newlogin=1; BAIDUID=A9BCC19BBD92EE870D57994815BCFED6:SL=0:NR=10:FG=1; H_PS_PSSID=60276_61027_61097_61178_61216_61206_61212_61208_61215_61242_61187_61281_61297; sug=3; sugstore=0; ORIGIN=0; bdime=0; BDUSS=NFUlBZVk40Q0F1YkF-S2FJWnpLUzVwWEJXb3NReGVObFN-N1JtSThMYklxM0puSVFBQUFBJCQAAAAAAQAAAAEAAAD2bJ2I2qPA79Gwy~vHp7DZtsgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMgeS2fIHktnbm; BDUSS_BFESS=NFUlBZVk40Q0F1YkF-S2FJWnpLUzVwWEJXb3NReGVObFN-N1JtSThMYklxM0puSVFBQUFBJCQAAAAAAQAAAAEAAAD2bJ2I2qPA79Gwy~vHp7DZtsgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMgeS2fIHktnbm; H_WISE_SIDS_BFESS=60276_61027_61097_61141_61178_61216_61206_61212_61208_61215_61242_61187_61281_61297; H_WISE_SIDS=60276_61027_61097_61178_61216_61206_61212_61208_61215_61242_61187_61281_61297; ab_sr=1.0.1_NThiNWVhYWZhZmYwNDdiZWE4OTk2MDdhMmEzNDJiZDJmOTI2MTJkNTJkNWM3NDJkM2UwZjY1NmQxOGIxOGU3NTlmNzFmNDFmYzBiMTM1NzA2YzEzOTA4ZDZkMjNmNDI0NTIwOTgwNTc0NWRmNWI0MjkzYzNmNGQ0NmZhNTIyNWViNzhjODEzYjY0YmM4NGY5MDkyZDg0YjgwMGRlZmM0NTYwYzMwNTAzYzU1ZWYzODVhMGZmNzU0NjNiMTYyZmY5; BA_HECTOR=21ak0g2k81210la520ak25003tsef31jko2ep1v; delPer=0; BD_CK_SAM=1; PSINO=7; BAIDUID_BFESS=A9BCC19BBD92EE870D57994815BCFED6:SL=0:NR=10:FG=1; ZFY=IZ8eC09M7uYS:Bgdyf0:A75jU3mCBxirsTbQR8nzfK5UA:C; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; RT="z=1&dm=baidu.com&si=5f05d4de-c557-4352-929a-90ce94ef3fbd&ss=m457pbm0&sl=e&tt=13e2&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1wcfs&ul=219e3&hd=219ek"; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_645EC=dd9c0cYJ4dC1kv6%2FP4i5cZSd2RikOfuIo8YInWLmvJYW5pD2bCjNZfWqMx1WhLJta0cC; BDSVRTM=333; baikeVisitId=f26208cf-7f41-4c69-b63c-ee08527465c5',
# 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
# }
#
# url = 'https://www.baidu.com/s'
#
# html = requests.get(url,headers=headers, params=params)
# html.encoding = 'utf-8'
#
# print(html.text)

# -----------------------pic
# picUrl = 'https://gimg3.baidu.com/topone/src=https%3A%2F%2Fbkimg.cdn.bcebos.com%2Fsmart%2F77094b36acaf2edda3ccb5bd185b16e93901213f3519-bkimg-process%2Cv_1%2Crw_1%2Crh_1%2Cmaxl_800%2Cpad_1%3Fx-bce-process%3Dimage%2Fresize%2Cm_pad%2Cw_348%2Ch_348%2Ccolor_ffffff&refer=http%3A%2F%2Fwww.baidu.com&app=2011&size=w931&n=0&g=0n&er=404&q=75&fmt=auto&maxorilen2heic=2000000?sec=1733158800&t=59f8004afb87ee7783762d7fef855c2b'
# image = requests.get(picUrl)
# with open('test.jpg', 'wb') as f:
#     f.write(image.content)

# ------------------------json
url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=7667330232466396892&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E4%BD%A0%E5%A5%BD&queryWord=%E4%BD%A0%E5%A5%BD&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&expermode=&nojc=&isAsync=&pn=90&rn=30&gsm=5a&1733040261097='
headers = {
'cookie': 'BDqhfp=%E4%BD%A0%E5%A5%BD%26%26NaN-1undefined%26%26816%26%262; BIDUPSID=A9BCC19BBD92EE878F22B7AD608A5AD1; PSTM=1731596290; newlogin=1; BAIDUID=A9BCC19BBD92EE870D57994815BCFED6:SL=0:NR=10:FG=1; H_PS_PSSID=60276_61027_61097_61178_61216_61206_61212_61208_61215_61242_61187_61281_61297; BDUSS=NFUlBZVk40Q0F1YkF-S2FJWnpLUzVwWEJXb3NReGVObFN-N1JtSThMYklxM0puSVFBQUFBJCQAAAAAAQAAAAEAAAD2bJ2I2qPA79Gwy~vHp7DZtsgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMgeS2fIHktnbm; BDUSS_BFESS=NFUlBZVk40Q0F1YkF-S2FJWnpLUzVwWEJXb3NReGVObFN-N1JtSThMYklxM0puSVFBQUFBJCQAAAAAAQAAAAEAAAD2bJ2I2qPA79Gwy~vHp7DZtsgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMgeS2fIHktnbm; H_WISE_SIDS=60276_61027_61097_61178_61216_61206_61212_61208_61215_61242_61187_61281_61297; BA_HECTOR=21ak0g2k81210la520ak25003tsef31jko2ep1v; delPer=0; PSINO=7; BAIDUID_BFESS=A9BCC19BBD92EE870D57994815BCFED6:SL=0:NR=10:FG=1; ZFY=IZ8eC09M7uYS:Bgdyf0:A75jU3mCBxirsTbQR8nzfK5UA:C; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; RT="z=1&dm=baidu.com&si=5f05d4de-c557-4352-929a-90ce94ef3fbd&ss=m457pbm0&sl=e&tt=13e2&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1wcfs&ul=219e3&hd=219ek"; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; H_WISE_SIDS_BFESS=60276_61027_61097_61178_61216_61206_61212_61208_61215_61242_61187_61281_61297; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=www.baidu.com; ab_sr=1.0.1_MGQ2YTVmMDE0Y2U0MGYwYTBiMWI4ODJiZjJiMzMzYWYyZWMzODhkNzViMDg1OWU3YjM0MGMxOWE4Y2E0MTU2NDNiNmNlZWZiZDRkOTYxZjgyMjc0N2EwNWFjOTViMWQzOTJiMzI2NTMwNWRkYzdhZjk3OTQzZGM3ZThkM2NmZGQzODdhZTI1MmNiZmQ5ODU5ZDBkNzA0Y2U5MmNlMzFhZA==; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm',
'referer': 'https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCwzLDEsMiwxMyw3LDYsNSwxMiw5&word=%E4%BD%A0%E5%A5%BD',
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
html = requests.get(url, headers=headers)
# print(html.json())
for i in html.json()['data']:
    if i:
        print(i['fromPageTitle'])