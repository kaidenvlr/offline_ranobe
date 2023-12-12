import requests

from bs4 import BeautifulSoup
import re
import json

from parser.utils.consts import chapters_json_pattern


def get_info(url):
    reqs = requests.session()
    info = {}
    page_html = reqs.get(url).text
    page = BeautifulSoup(page_html, "lxml")
    info["title"] = page.find("div", {"class": "media-name__main"}).text.strip()
    info["description"] = page.find("div", {"class": "media-description__text"}).text.strip()
    info["authors"] = [x.text.strip() for x in page.find("div", string="Автор").parent.find_all("a")]
    info["tags"] = [x.text.strip().title() for x in page.find("div", {"class": "media-tags"}).find_all("a")]
    info["poster_url"] = page.find("div", {"class": "media-sidebar__cover paper"}).find("img")["src"]
    chapters = re.search(chapters_json_pattern, page_html).group(1)
    chapters = json.loads(chapters)
    # -------------------
    info["chapters"] = {}
    for c in reversed(chapters["chapters"]["list"]):
        if str(c["chapter_volume"]) not in info["chapters"]:
            info["chapters"][str(c["chapter_volume"])] = []
        info["chapters"][str(c["chapter_volume"])].append(c)
    return info
