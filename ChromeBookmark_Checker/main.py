import requests
import time

with open(r'E:\Document\Download\bookmarks_2020_07_17.html', 'r', encoding='utf-8') as f:
    data = f.readlines()


errors = []
for d in data:
    url, title = d.split('\t')
    r = requests.get(url)
    if r.status_code != requests.codes.ok:
        with open(r'E:\Document\Download\bookmarks_2020_07_17.text', 'a', encoding='utf-8') as f:
            f.write('\n' + title)
        print(r.status_code, title)
    time.sleep(0.05)
