import bs4
import requests

# 下载网页
response = requests.get("http://data.2018.163.com/scoreboard.html")
try:
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, features="html.parser")
    # Find the name of the Team.group
    # design CSS Selectors For <table groupname="A">
    print(response.text)
    groupNameList = soup.select("[groupname]")
    for groupName in groupNameList:
        print(groupName)
except Exception as exception:
    print(exception)
