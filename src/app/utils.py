import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode, urljoin, urlparse, urlunparse, parse_qs, urlencode

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
        resp = requests.get(url, headers=HEADERS, timeout=15, verify=False)
        return (get_title(resp.text), resp.url)
    except Exception as e:
        return ('BAD_LINK', '')


BLACK_LISTED = ['source', 'gi', 'feature', '__twitter_impression',
                'gws_rd', 'ab_channel', 'feature', 'utm_source', 'ref', '_p', 'referralCode', 'utm_medium',
                'utm_campaign', 'app', 'couponCode', 'fbclid', 'utm_content', '_saasquatch', 'igshid', 'linkCode', 'refcode']


def clean_up_url(url):
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)
    keys = [k for k in qs.keys()]
    for k in keys:
        if k in BLACK_LISTED:
            del qs[k]
    new_query = urlencode(qs, doseq=1)

    return urlunparse([parsed.scheme, parsed.netloc, parsed.path, parsed.params, new_query, parsed.fragment])
