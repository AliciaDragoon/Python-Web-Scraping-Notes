import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor


def get_img_url():
    for page in range(1, 11):
        url = f"https://www.pkdoutu.com/article/list/?page={page}"
        headers = {
            "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
                "Safari/537.36 Edg/120.0.0.0",
        }
        resp = requests.get(url, headers=headers)
        tree = etree.HTML(resp.text)
        img_urls = tree.xpath(
            "//li[@class= 'list-group-item']//img/@data-original")  # 图片存储在data-original中，而不是页面源代码的src中
        with ThreadPoolExecutor(16) as t:
            for img_url in img_urls:
                # print(img_url)
                # download_img(img_url)
                t.submit(download_img, img_url)


def download_img(url):
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
            "Safari/537.36 Edg/120.0.0.0",
    }
    resp = requests.get(url, headers=headers)
    file_name = url.split("/")[-1]
    with open(file_name, mode="wb") as f:
        f.write(resp.content)
    print("已下载一张图片")


if __name__ == '__main__':
    get_img_url()
