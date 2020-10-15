from flask import jsonify
from app import app


@app.route('/', methods=['GET'])
def index():
    return jsonify({'status': 'OK'})
