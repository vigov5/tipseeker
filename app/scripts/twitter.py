import sys
sys.path.append('../../')  # nopep8

import tweepy
from app.link.models import Link
from app.link import constants as LINK
from app.utils import get_title, link_expander, clean_up_url


def fetch_twitter(twitter_api, query):
    print('Start fetch twitter with query {}'.format(query))
    for tweet_info in tweepy.Cursor(twitter_api.search, q=query, lang='en', tweet_mode='extended').items(100):
        retweeted_status = False
        media = ''
        links = []
        if 'retweeted_status' in dir(tweet_info):
            retweeted_status = True
            tweet = tweet_info.retweeted_status.full_text
            if 'media' in tweet_info.retweeted_status.entities:
                for m in tweet_info.retweeted_status.entities['media']:
                    media = m['media_url']
            for u in tweet_info.retweeted_status.entities['urls']:
                links.append(u['expanded_url'])
                tweet = tweet.replace(u['url'], u['expanded_url'])
        else:
            tweet = tweet_info.full_text
            if 'media' in tweet_info.entities:
                for m in tweet_info.entities['media']:
                    media = m['media_url']
            for u in tweet_info.entities['urls']:
                links.append(u['expanded_url'])
                tweet = tweet.replace(u['url'], u['expanded_url'])

            created = False
            for idx, item in enumerate(links):
                link_info = {}
                (title, final_url) = link_expander(item)
                final_url = clean_up_url(final_url)
                if Link.query.filter(Link.url == final_url).first():
                    pass
                else:
                    link_info['origin'] = "https://twitter.com/i/web/status/{}#link{}".format(
                        tweet_info.id, idx)
                    if title != "BAD_LINK":
                        link_info['title'] = title.encode('utf-8')
                        link_info['url'] = final_url
                        link_info['status'] = LINK.STATUS_DONE
                        link_info['media'] = media
                        link_info['content'] = tweet.encode('utf-8')
                        link_info['read'] = LINK.UNREAD
                        link_info['kind'] = LINK.KIND_LINK
                        link_info['category'] = LINK.CATEGORY_WEB
                        link_info['created_at'] = tweet_info.created_at
                        Link.insert_from(link_info)
                        created = True

            if not created and not Link.query.filter(Link.content == tweet.encode('utf-8')).first():
                link_info = {}
                link_info['title'] = 'Tip from Twitter'
                link_info['url'] = "https://twitter.com/i/web/status/{}".format(
                    tweet_info.id)
                link_info['origin'] = link_info['url']
                link_info['status'] = LINK.STATUS_DONE
                link_info['media'] = media
                link_info['content'] = tweet.encode('utf-8')
                link_info['read'] = LINK.UNREAD
                link_info['kind'] = LINK.KIND_LINK
                link_info['category'] = LINK.CATEGORY_WEB
                link_info['created_at'] = tweet_info.created_at
                Link.insert_from(link_info)
