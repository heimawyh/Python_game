import urllib.request
import requests

url = "https://www.bilibili.com"


# 访问
def use_urllib(url):
    response = urllib.request.urlopen(url)
    data = response.read().decode()
    print(data)
def use_requests(url):
    response = requests.get(url)
    data = response.text
    print(data)

if __name__ == '__main__':
    # use_urllib(url)
    use_requests(url)
