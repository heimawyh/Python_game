import urllib.request
import requests


url = "https://www.bilibili.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"
}


# 访问
def use_urllib(url):
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    data = response.read().decode()
    print(data)


def use_requests(url):
    response = requests.get(url, headers=headers)
    data = response.text
    # print(data)
    filePath = "bilibili.html"
    with open(filePath,"w",encoding="utf-8")as f:
        f.write(data)

if __name__ == '__main__':
    # use_urllib(url)
    use_requests(url)
