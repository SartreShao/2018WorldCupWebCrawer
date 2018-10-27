import re
import leancloud

from selenium import webdriver

leancloud.init("wNtRKa0HKCdK3vatV6MfAPVM-gzGzoHsz", "VV83Te9eHKmdkc8mydAWV2jR")
browser = webdriver.Chrome()
browser.get("http://data.2018.163.com/all_player.html#/data")
Player = leancloud.Object.extend("Player")
Team = leancloud.Object.extend("Team")


def print_in_console():
    table = browser.find_elements_by_tag_name("table")
    for item in table:
        for tr in item.find_elements_by_tag_name("tr"):
            i = 0
            for td in tr.find_elements_by_tag_name("td"):
                if i == 3:
                    print()
                    break
                i = i + 1
                print(td.text, end=" ")


def output_to_leancloud():
    table = browser.find_elements_by_tag_name("table")
    for item in table:
        for tr in item.find_elements_by_tag_name("tr"):
            i = 0
            player_num = None
            player_name = None
            team_name = None
            for td in tr.find_elements_by_tag_name("td"):
                if i == 0:
                    player_num = td.text
                    print("球员编号" + player_num, end=" ")
                if i == 1:
                    player_name = td.text
                    print("球员姓名" + player_name, end=" ")
                if i == 2:
                    team_name = td.text
                    print("球队名称" + team_name, end=" ")
                if i == 3:
                    # 查询team id
                    query = leancloud.Query("Team")
                    query_result = query.equal_to("name", team_name).find()
                    team_id = query_result[0].id
                    team = Team.create_without_data(team_id)
                    # 存储
                    player = Player()
                    player.set('name', player_name)
                    player.set('shirt_number', int(player_num))
                    player.set('team', team)
                    player.save()
                    print()
                    break
                i = i + 1

            # print(td.text, end=" ")


try:
    print_in_console()
    # output_to_leancloud()

except Exception as exception:
    print(exception)
