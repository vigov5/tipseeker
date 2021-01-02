from flask import Blueprint, jsonify, request
from sqlalchemy import desc, func

from app import app, db
from app.link.models import Link
from app.link import constants as LINK

link_module = Blueprint('link', __name__)


@link_module.route('/', methods=['GET'])
@link_module.route('/all', methods=['GET'])
def index():
    try:
        page = int(request.args.get('page'))
        links = Link.query.filter(Link.read == LINK.UNREAD).order_by(desc(Link.id)).paginate(
            page=page, per_page=10).items
    except Exception as e:
        print(e)
        page = 1
        links = []

    return jsonify({'unread_count': Link.get_unread_count(), 'links': links})


@link_module.route('/mark_read', methods=['POST'])
def mark_read():
    try:
        params = request.get_json(force=True)
        link = Link.query.get(params['id'])
        link.rating = LINK.HELPFUL if params['rating'] else LINK.SPAM
        link.read = LINK.READ
        db.session.add(link)
        db.session.commit()
        return jsonify({'status': 'OK', 'unread_count': Link.get_unread_count()})
    except Exception as e:
        return jsonify({'status': 'Error', 'msg': str(e)})
