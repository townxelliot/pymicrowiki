# GET / - list all pages and files as links to /pages/:id and /files/:id respectively

# GET /pages/ - list all pages; show form to create a new page

# GET /files/ - list all files; show form to enable uploading a new file

# POST /pages/ - create a page with a new ID

# POST /files/ (with file upload in body) - create a new file on the server

# GET /pages/:id - show a page in editor

# GET /files/:id - show details of a file with download link

from flask import Blueprint, redirect, render_template, request, url_for

from pymicrowiki.db import get_db
from pymicrowiki.models import Page

mainroutes = Blueprint('mainroutes', __name__)


@mainroutes.route('/', methods=['GET'])
def home():
    pages = get_db().query(Page).order_by(Page.content).all()

    ctx = {
      'pages': list(map(lambda page: {'id': page.id, 'content': page.content}, pages)),
      'files': [],
    }

    return render_template('home.tpl.html', **ctx)

@mainroutes.route('/pages/', methods=['POST'])
def pages():
    # save the page to db
    get_db().add(Page(content=request.form['content']))

    # return to home page
    return redirect(url_for('mainroutes.home'))

@mainroutes.route('/pages/<id>', methods=['GET', 'POST'])
def page(id):
    if request.method == 'GET':
        page = get_db().query(Page).filter(Page.id==id).first()

        ctx = {
          'id': page.id,
          'content': page.content,
        }

        return render_template('page.tpl.html', **ctx)

    if request.method == 'POST' and request.form['action'] == 'Delete':
        get_db().delete(Page, id)
        return redirect(url_for('mainroutes.home'))
