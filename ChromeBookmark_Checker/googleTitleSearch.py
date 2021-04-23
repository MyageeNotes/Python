import requests
import time
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html5lib")
    return response, soup


with open(r'E:\Document\Download\bookmarks_2020_07_17.text', 'r', encoding='utf-8') as f:
    data = f.readlines()

print(len(data))

for title in data:
    print(title)
    url = "{}{}".format(r"https://www.google.com/search?q=", title)
    print(url)
    rp, sp = get_html(url)
    print(rp, sp)
    categories = sp.select("#rso div.g div.rc div.r a")
    print(categories)
    exit()
    for category in categories:
        print(category)
        url = category.get("href")
        print(url)
        with open(r'E:\Document\Download\bookmarks_2020_07_17_titleSearch.txt', 'a', encoding='utf-8') as f:
            f.write('\n{}\t{}'.format(title, url))
            print(title, url)