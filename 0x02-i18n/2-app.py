#!/usr/bin/env python3
"""Get locale from request"""

from flask import Flask, render_template
from flask_babel import Babel
from requests import request

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    """Babel configuration"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/", methods=['GET'], strict_slashes=False)
def index() -> str:
    """render template for Babel usage"""
    return render_template('2-index.html')


@babel.localeselector
def get_locale() -> str:
    """determine the best match with supported lang."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
