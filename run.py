from app import app as application
from app import app
import sys
import logging
logging.basicConfig(stream=sys.stderr)

if __name__ == '__main__':
    import logging
    logging.basicConfig(filename='error.log', level=logging.DEBUG)
    app.run(host='0.0.0.0', debug=True, port=5001)
