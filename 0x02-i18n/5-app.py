#!/usr/bin/env python3
'''Basic Flask Setup
'''

from typing import Dict, Union
from flask import Flask, render_template, request, g
from flask_babel import Babel

class Config:
    '''Configuration class                                                                                                                           
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)

app.config.from_object(Config)

babel = Babel()

babel.init_app(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    '''default route'''
    return render_template('5-index.html')

@babel.localeselector
def get_locale() -> str:
    '''determine the best match with our supported languages.
    '''
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user() -> Union[Dict, None]:
    '''returns a user dictionary or None if the ID cannot be found or if login_as was not passed
    '''
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None

@app.before_request
def before_request() -> None:
    '''executed first
    '''
    g.user = get_user()


if __name__ == "__main__":
    app.run(debug=True)
