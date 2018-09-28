import bs4
import requests

response = requests.get("https://www.baidu.com")
try:
    response.raise_for_status()
    baiduSoup = bs4.BeautifulSoup(response.text)
except Exception as exception:
    print(exception)
