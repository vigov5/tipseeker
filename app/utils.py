import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urlunparse

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1'
}

RED_ONE = ['medium.com']
BLUE_ONE = ['youtube.com']


def get_title(content):
    soup = BeautifulSoup(content, 'html.parser')
    og_title = soup.find('meta', attrs={'property': 'og:title'})
    if og_title:
        return og_title['content']
    if soup.find('title'):
        return soup.find('title').text
    else:
        return ''


def link_expander(url, origin='twitter'):
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        return (get_title(resp.text), resp.url)
    except Exception as e:
        return ('BAD_LINK', '')


def clean_up_url(url):
    parsed = urlparse(url)
    if parsed.netloc in RED_ONE:
        return urljoin(url, parsed.path)
    elif parsed.netloc in BLUE_ONE:
        return urlunparse([parsed.scheme, parsed.netloc, '', '', parsed.query, ''])
    else:
        return url
