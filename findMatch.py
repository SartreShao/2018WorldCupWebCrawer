import re

import leancloud
from selenium import webdriver

leancloud.init("wNtRKa0HKCdK3vatV6MfAPVM-gzGzoHsz", "VV83Te9eHKmdkc8mydAWV2jR")
Team = leancloud.Object.extend("Team")
Match = leancloud.Object.extend("Match")
browser = webdriver.Chrome()

# 打印小组赛数据
# browser.get("http://data.2018.163.com/schedule.html#/group")
# i = 1
# try:
#     table = browser.find_elements_by_tag_name("table")
#     for item in table:
#         for tr in item.find_elements_by_tag_name("tr"):
#             i = 0
#             is_group_match = True
#             starting_time = None
#             away_team_name = None
#             home_team_name = None
#             away_team_goals = None
#             home_team_goals = None
#             for td in tr.find_elements_by_tag_name("td"):
#                 if i == 1:
#                     starting_time = td.text
#                 if i == 3:
#                     pattern = '([\u4e00-\u9fa5]*)([0-9]*)-([0-9]*)([\u4e00-\u9fa5]*)'
#                     result = re.match(pattern, td.text)
#                     if result is not None:
#                         away_team_name = result.group(1)
#                         away_team_goals = result.group(2)
#                         home_team_goals = result.group(3)
#                         home_team_name = result.group(4)
#                     print("开始时间: " + starting_time)
#                     print("客场球队名：" + away_team_name, end=" ")
#                     print("主场球队名：" + home_team_name, end=" ")
#                     print("客场进球数：" + away_team_goals, end=" ")
#                     print("主场球队名：" + home_team_goals, end=" ")
#                 if i == 4:
#                     # 查询home_team
#                     query = leancloud.Query("Team")
#                     query_result = query.equal_to("name", home_team_name).find()
#                     home_team_id = query_result[0].id
#                     home_team = Team.create_without_data(home_team_id)
#                     # 查询away_team
#                     query_result = query.equal_to("name", away_team_name).find()
#                     away_team_id = query_result[0].id
#                     away_team = Team.create_without_data(away_team_id)
#                     # 存储
#                     match = Match()
#                     match.set('away_team', away_team)
#                     match.set('away_team_goals', int(away_team_goals))
#                     match.set('home_team', home_team)
#                     match.set('home_team_goals', int(home_team_goals))
#                     match.set('is_group_match', is_group_match)
#                     match.set('starting_time', starting_time)
#                     match.save()
#                     print(home_team)
#                     break
#                 i = i + 1
#                 # if (i != 0) & (i != 2):
#                 # print(td.text, end=" ")
# except Exception as exception:
#     print(exception)

# 打印淘汰赛数据
browser.get("http://data.2018.163.com/schedule.html#/eliminate")
i = 1
try:
    table = browser.find_elements_by_tag_name("table")
    for item in table:
        for tr in item.find_elements_by_tag_name("tr"):
            i = 0
            is_group_match = False
            starting_time = None
            away_team_name = None
            home_team_name = None
            away_team_goals = None
            home_team_goals = None
            for td in tr.find_elements_by_tag_name("td"):
                if i == 1:
                    starting_time = td.text
                if i == 3:
                    pattern = '([\u4e00-\u9fa5]*)([0-9]*)-([0-9]*)([\u4e00-\u9fa5]*)'
                    result = re.match(pattern, td.text)
                    if result is not None:
                        away_team_name = result.group(1)
                        away_team_goals = result.group(2)
                        home_team_goals = result.group(3)
                        home_team_name = result.group(4)
                    print("开始时间: " + starting_time)
                    print("客场球队名：" + away_team_name, end=" ")
                    print("主场球队名：" + home_team_name, end=" ")
                    print("客场进球数：" + away_team_goals, end=" ")
                    print("主场球队名：" + home_team_goals, end=" ")
                if i == 4:
                    # 查询home_team
                    query = leancloud.Query("Team")
                    query_result = query.equal_to("name", home_team_name).find()
                    home_team_id = query_result[0].id
                    home_team = Team.create_without_data(home_team_id)
                    # 查询away_team
                    query_result = query.equal_to("name", away_team_name).find()
                    away_team_id = query_result[0].id
                    away_team = Team.create_without_data(away_team_id)
                    # 存储
                    match = Match()
                    match.set('away_team', away_team)
                    match.set('away_team_goals', int(away_team_goals))
                    match.set('home_team', home_team)
                    match.set('home_team_goals', int(home_team_goals))
                    match.set('is_group_match', is_group_match)
                    match.set('starting_time', starting_time)
                    match.save()
                    print(home_team)
                    break
                i = i + 1
except Exception as exception:
    print(exception)
