from selenium import webdriver

# # 打印小组赛数据
browser = webdriver.Chrome()
# browser.get("http://data.2018.163.com/schedule.html#/group")
# i = 1
# try:
#     table = browser.find_elements_by_tag_name("table")
#     for item in table:
#         for tr in item.find_elements_by_tag_name("tr"):
#             i = 0
#             for td in tr.find_elements_by_tag_name("td"):
#                 if i == 4:
#                     print()
#                     break
#                 i = i + 1
#                 # if (i != 0) & (i != 2):
#                 print(td.text, end=" ")
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
            for td in tr.find_elements_by_tag_name("td"):
                if i == 4:
                    print()
                    break
                i = i + 1
                print(td.text, end=" ")
except Exception as exception:
    print(exception)
