import requests
from datetime import datetime
import sys
sys.path.append('../../')  # nopep8

import cssutils
from bs4 import BeautifulSoup
import json
from app.link import constants as LINK
from app.link.models import Link
from app.utils import get_title, link_expander, remove_query_str


def fetch_telegram(url, page_name):
    print('Start fetch {}: {}'.format(page_name, url))
    s = requests.Session()
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:71.0) Gecko/20100101 Firefox/71.0'
    }
    resp = s.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    soup = soup.find_all("div", {"class": "tgme_widget_message_bubble"})
    for i in range(len(soup)):
        info_post = soup[i].find_all(
            "div", {"class": "tgme_widget_message_info"})
        mess_text = soup[i].find_all(
            "div", {"class": "tgme_widget_message_text"})
        content = BeautifulSoup(str(mess_text[0]), 'html.parser')
        info_post = BeautifulSoup(str(info_post[0]), 'html.parser')
        media = soup[i].find_all("i", {"class": "link_preview_image"})

        content = content.find_all('a')[0]
        url = content.get('href')
        origin = info_post.find_all('a')[0].get('href')
        content = str(mess_text[0].get_text())[:-len(url)]
        post_time = info_post.find_all('time')[0].get('datetime')
        if media != []:
            div_style = BeautifulSoup(
                str(media[0]), 'html.parser').find('i')['style']
            style = cssutils.parseStyle(div_style)
            url_image = style['background-image']
            url_image = url_image[4:-1]
        else:
            url_image = ''
        info = {"category": LINK.CATEGORY_WEB,
                "content": content,
                "created_at": datetime.fromisoformat(post_time),
                "kind": LINK.KIND_LINK,
                "media": url_image,
                "origin": origin,
                "read": LINK.UNREAD,
                "status": LINK.STATUS_DONE,
                "title": page_name,
                "url": url}
        if Link.query.filter(Link.url == info['url']).first():
            continue
        else:
            Link.insert_from(info)
