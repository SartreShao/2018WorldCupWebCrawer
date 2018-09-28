import requests

response = requests.get("https://www.baidu.com")
# noinspection PyBroadException
try:
    response.raise_for_status()
    print(type(response.text))
    file = open("baidu.html", "wb")
    print(type(file))
    for chuck in response.iter_content(100000):
        file.write(chuck)
    file.close()
except Exception as exception:
    print(exception)
