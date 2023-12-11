import ssl
import urllib.request
from bs4 import BeautifulSoup

url = "https://desk.zol.com.cn/pc/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/78.0.3904.97 Safari/537.36'}
ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
ctx.options |= 0x4

add = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(url=add, timeout=10, context=ctx)

main_page_source = response.read().decode('gbk')
# print(main_page_source)

main_page = BeautifulSoup(main_page_source, "html.parser")
main_page.select("")
