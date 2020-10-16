# Tipseeker

Simple app to gather all #bugbountytips from Twitter and Telegram.

![screenshot](https://i.imgur.com/4BuzAM5l.png)

## Backend
- require Python >= 3.6

```
virtualenv --python=python3 venv
source venv/bin/active
pip install -r requirements.txt
```

- Copy `config.sample.py` to `config.py` and update values. `CONSUMER_KEY` and `CONSUMER_SECRET` is your Twitter app creds.
- Create DB, change DB creds in `SQLALCHEMY_DATABASE_URI` and run:

```
alembic upgrade head
```

- Final, deploy with `gunicorn`.

## Frontend

copy `frontend/src/config.sample.js` to `frontend/src/config.js` and change `BASE_URL` to deployed API URL.

```
cd frontend
yarn install
yarn build
```

Deploy `frontend/public` to static hosting site like Surge, Netlify.

## Cron

Every 5 minutes

```
*/5 * * * * FLASK_APP=/path/to/tipseeker/app /path/to/tipseeker/venv/bin/python3 -m flask cron telegram
```

## Roadmap

- [ ] Better filtering
- [ ] Chrome/Firefox extension send link to app
- [ ] Apply NLP to detect if tip is worth reading
- [ ] More source
