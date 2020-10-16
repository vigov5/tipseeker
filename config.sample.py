import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/db?charset=utf8mb4'

CSRF_ENABLED = True
SECRET_KEY = 'place_your_csrf_session_key_here'
CSRF_SESSION_KEY = 'place_your_csrf_key_here'

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
TWITTER_QUERY = '#bugbountytips'

TELEGRAM_CHANNELS = [
    ('https://t.me/s/thebugbountyhunter', 'The Bug Bounty Hunter')
]
