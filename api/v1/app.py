#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import environ


try:
    hbnb_host = environ['HBNB_API_HOST']
    hbnb_port = environ['HBNP_API_PORT']
except:
    hbnb_host = '0.0.0.0'
    hbnb_port = '5000'

app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
app.env = 'development'
app.config.update(JSONIFY_PRETTYPRINT_REGULAR=True)


@app.teardown_appcontext
def teardown_appcont(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == "__main__":
    app.run(host=hbnb_host, port=hbnb_port, threaded=True)
