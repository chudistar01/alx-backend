#!/usr/bin/env python3
'''Basic Flask Setup
'''

from flask import Flask, render_template, request, render_template_string
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
    return render_template('3-index.html')

@babel.localeselector
def get_locale() -> str:
    '''determine the best match with our supported languages.
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(debug=True)
