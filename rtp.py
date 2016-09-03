from urllib import request
from bs4 import BeautifulSoup

url = "http://media.rtp.pt/praca/rubricas/culinaria/page/"
recipe_pages = []

for _p in range(1, 21):
    _pc = request.urlopen(request.Request(url + str(_p), headers={'User-Agent': 'Mozilla'})).read()
    _s = BeautifulSoup(_pc, "html.parser")
    _f = _s.find_all("article", class_="col-sm-6", recursive=True)
    for i in _f:
        recipe_pages.append(i.contents[1].attrs["href"])

_k = 0
for recipe_page in recipe_pages:
    _pc = request.urlopen(request.Request(recipe_page, headers={'User-Agent': 'Mozilla'})).read()
    _ss = BeautifulSoup(_pc, "html.parser")
    _t = _ss.find("title").getText().replace('|', '').replace('Praça', '').replace('RTP', '').rstrip().replace(' ', '_')
    _ff = _ss.find("div", class_="entry-content").getText()
    with open("output/" + "rtp_" + str(_k) + "_" + _t + ".txt", "w") as f:
        f.write(_t.replace('_', ' ') + "\n")
        f.write(_ff)
        print("Wrote {}.".format(_t))
    _k += 1
