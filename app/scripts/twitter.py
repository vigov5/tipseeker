from app.scripts import cron_module
from app.utils import get_title, link_expander, clean_up_url
from app.link import constants as LINK
from app.link.models import Link
from app import app, twitter_api
from difflib import SequenceMatcher
import tweepy
import sys
sys.path.append('../../')  # nopep8
import urllib3

urllib3.disable_warnings()


@cron_module.cli.command('twitter')
def fetch_twitter():
    query = app.config['TWITTER_QUERY']
    print('Start fetch twitter with query {}'.format(query))
    cached_contents = [content for (
        content, ) in Link.query.with_entities(Link.content).all()]

    for tweet_info in tweepy.Cursor(twitter_api.search, q=query, lang='en', tweet_mode='extended').items(100):
        media = ''
        links = []
        origin_tweet = ''
        if 'retweeted_status' in dir(tweet_info):
            tweet = tweet_info.retweeted_status.full_text
            if 'media' in tweet_info.retweeted_status.entities:
                for m in tweet_info.retweeted_status.entities['media']:
                    media = m['media_url']
            for u in tweet_info.retweeted_status.entities['urls']:
                links.append(u['expanded_url'])
                tweet = tweet.replace(u['url'], u['expanded_url'])

            origin_tweet = "https://twitter.com/i/web/status/{}".format(
                tweet_info.retweeted_status.id)
        else:
            tweet = tweet_info.full_text
            if 'media' in tweet_info.entities:
                for m in tweet_info.entities['media']:
                    media = m['media_url']
            for u in tweet_info.entities['urls']:
                links.append(u['expanded_url'])
                tweet = tweet.replace(u['url'], u['expanded_url'])
            origin_tweet = "https://twitter.com/i/web/status/{}".format(
                tweet_info.id)

        tweet_content = tweet.encode('utf-8')

        similar_content = False
        ignored_content = False
        for c in cached_contents:
            if SequenceMatcher(None, c, tweet_content).ratio() >= 0.6:
                similar_content = True
                break

        for kw in app.config['IGNORED_KEYWORDS']:
            if kw in tweet_content.lower():
                ignored_content = True
                break

        created = False
        for idx, item in enumerate(links):
            link_info = {}
            (title, final_url) = link_expander(item)
            final_url = clean_up_url(final_url)
            if Link.query.filter(Link.url == final_url).first() or similar_content or ignored_content:
                created = True
                pass
            else:
                link_info['origin'] = "{}#link{}".format(origin_tweet, idx)
                if title != "BAD_LINK":
                    link_info['title'] = title.encode('utf-8')
                    link_info['url'] = final_url
                    link_info['status'] = LINK.STATUS_DONE
                    link_info['media'] = media
                    link_info['content'] = tweet_content
                    link_info['read'] = LINK.UNREAD
                    link_info['kind'] = LINK.KIND_LINK
                    link_info['category'] = LINK.CATEGORY_WEB
                    link_info['created_at'] = tweet_info.created_at
                    Link.insert_from(link_info)
                    created = True
        tweet_url = origin_tweet

        same_url = Link.query.filter(Link.url == tweet_url).first() != None

        print("{} -> Created: {}, Similar content: {}, Same URL: {}".format(
            tweet_url, created, similar_content, same_url
        ))
        cached_contents.append(tweet_content)

        if not created and not similar_content and not same_url and not ignored_content:
            link_info = {}
            link_info['title'] = 'Tip from Twitter'
            link_info['url'] = tweet_url
            link_info['origin'] = tweet_url
            link_info['status'] = LINK.STATUS_DONE
            link_info['media'] = media
            link_info['content'] = tweet_content
            link_info['read'] = LINK.UNREAD
            link_info['kind'] = LINK.KIND_LINK
            link_info['category'] = LINK.CATEGORY_WEB
            link_info['created_at'] = tweet_info.created_at
            Link.insert_from(link_info)
