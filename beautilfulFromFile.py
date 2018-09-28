import bs4

exampleFile = open("example.html")
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), features="html.parser")
author = exampleSoup.select("#author")
for item in author:
    print(item)
