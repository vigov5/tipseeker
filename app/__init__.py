import tweepy
from flask import Flask, Blueprint
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
CORS(app)


from app.scripts.twitter import fetch_twitter  # nopep8
from app.scripts.telegram import fetch_telegram  # nopep8

twitter_auth = tweepy.OAuthHandler(
    app.config['CONSUMER_KEY'], app.config['CONSUMER_SECRET'])
twitter_api = tweepy.API(twitter_auth)

scheduler = BackgroundScheduler()
scheduler.add_job(func=fetch_twitter, args=[
                  twitter_api, app.config['TWITTER_QUERY']], trigger="interval", seconds=app.config['INTERVAL'])

for idx, (url, page_name) in enumerate(app.config['TELEGRAM_CHANNELS']):
    scheduler.add_job(func=fetch_telegram, args=[
                      url, page_name], trigger="interval", seconds=app.config['INTERVAL'] + idx*5)
scheduler.start()

from app.link.views import link_module  # nopep8
app.register_blueprint(link_module, url_prefix='/link')
