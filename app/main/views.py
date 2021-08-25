from flask import render_template, request
from flask_login import login_required, current_user
from . import main
import requests
from .forms import BlogForm
from .. import db
from ..models import Blog


@main.route('/', methods=['GET', 'POST'])
def index():
    quotes_response = requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()
    print(quotes_response)
    return render_template('index.html', quotes_response=quotes_response)


@main.route('/blog/all/', methods=['GET', 'POST'])
def all_blogs():
    return render_template('all-blogs.html')


@main.route('/blog/new/', methods=['GET', 'POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title
        description = form.description
        owner_id = current_user.id

        blog = Blog(title=title, description=description, owner_id=owner_id)

        db.session.add(blog)
        db.session.commit()

    return render_template('new-blog.html', form=form)


@main.route('/blog/<int:id>/', methods=['GET', 'POST'])
def blog(id):
    return render_template('blog.html')

