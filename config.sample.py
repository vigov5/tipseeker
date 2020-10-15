import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/db'

CSRF_ENABLED = True
SECRET_KEY = 'place_your_csrf_session_key_here'
CSRF_SESSION_KEY = 'place_your_csrf_key_here'

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
TWITTER_QUERY = ''
TWITTER_QUERY = ''

TELEGRAM_CHANNELS = [
    ('https://t.me/s/xxxxxx', 'Channel Name')
]

INTERVAL = 60
