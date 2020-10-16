import tweepy
from flask import Flask, Blueprint
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
CORS(app)

twitter_auth = tweepy.OAuthHandler(
    app.config['CONSUMER_KEY'], app.config['CONSUMER_SECRET'])
twitter_api = tweepy.API(twitter_auth)


from app.link.views import link_module  # nopep8
from app.scripts import cron_module  # nopep8
app.register_blueprint(link_module, url_prefix='/link')
app.register_blueprint(cron_module)
