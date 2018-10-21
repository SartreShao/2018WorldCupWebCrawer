from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://data.2018.163.com/scoreboard.html")
try:
    # 寻找 标签名：table name=A中的内容
    table = browser.find_elements_by_tag_name("table")
    for item in table:
        print(item.get_attribute("groupname"))

    # urls = browser.find_elements_by_xpath("//a")
    # for url in urls:
    #     print(url.text)
    # a = browser.find_element_by_link_text("http://2018.163.com/speecial/team4725")
    # print(a.text)
except Exception as exception:
    print(exception)
    print("Was Not Able To Find An Element With That Name.")
