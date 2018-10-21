from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://data.2018.163.com/all_player.html#/data")
i = 1
try:
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
except Exception as exception:
    print(exception)
