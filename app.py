"""
data model:

Page
* content
"""

from os import path

from flask import Flask

from pymicrowiki.blueprint import mainroutes


def create_app():
    app = Flask(__name__)

    app.register_blueprint(mainroutes)

    return app

if __name__ == '__main__':
    create_app().run()
