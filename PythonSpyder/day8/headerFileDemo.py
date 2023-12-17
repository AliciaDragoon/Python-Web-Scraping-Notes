import requests

url = "https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919"
headers = {
    "Cookie": "##########",
    # 放入经验证的cookies（从浏览器端复制一个）
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  "Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"}
# 该头文件只对老网站有效

resp = requests.get(url, headers=headers)
print(resp.text)
