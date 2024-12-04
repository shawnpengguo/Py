import httpx
import ddddocr

# 案例网站也过期了 后续有类似补一下

login_url = ""

headers = {}

session = httpx.Client()
session.headers.update(headers)