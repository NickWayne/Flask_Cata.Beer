import os
from flask import Flask, render_template, url_for
from . import dangerous_session_interface

from .home import home

from database import mongo

app = Flask(__name__)
app.config['DEBUG'] = True
app.config.from_object('config')
app.session_interface = dangerous_session_interface.ItsdangerousSessionInterface()

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

mongo.init_app(app)

app.register_blueprint(home)

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if 'static' in endpoint.split('.'):
        filename = values.get('filename', None)
        if filename:
            slash_endpoint = os.path.sep.join(endpoint.split('.'))
            file_path = os.path.join(app.root_path,
                                     slash_endpoint, filename)

            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html", e=e), 500

try:
    app.secret_key = os.environ['SECRET_KEY']
except KeyError:
    app.secret_key = "1y2398yaskf"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
