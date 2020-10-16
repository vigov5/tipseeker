from flask import Blueprint

cron_module = Blueprint('cron', __name__)

import app.scripts.telegram  # nopep8
import app.scripts.twitter  # nopep8
