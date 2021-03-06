"""
data model:

Page
* content
"""

from os import path

from flask import Flask

from pymicrowiki.blueprint import mainroutes
from pymicrowiki.jinja import linkerise, linkerise_or_show


def create_app():
    app = Flask(__name__)

    app.register_blueprint(mainroutes)

    # Jinja filters
    app.jinja_env.filters['linkerise'] = linkerise
    app.jinja_env.filters['linkerise_or_show'] = linkerise_or_show

    return app

if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=5005)
