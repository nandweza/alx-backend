"""Basic Babel setup"""

import babel
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


@app.route("/")
def index():
    """returns index.html"""
    return render_template('1-index.html')

babel = Babel(app)

class Config(object):
    LANGUAGES = ['en', 'fr']

if __name__ == '__main__':
    app.run(debug=True)