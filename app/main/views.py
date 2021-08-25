from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from . import main
import requests
from .forms import BlogForm, CommentForm
from .. import db
from ..models import Blog, Comment


@main.route('/', methods=['GET', 'POST'])
def index():
    quotes_response = requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()
    print(quotes_response)
    return render_template('index.html', quotes_response=quotes_response)


@main.route('/blog/all/', methods=['GET', 'POST'])
def all_blogs():
    blogs = Blog.query.all()
    return render_template('all-blogs.html', blogs=blogs)


@main.route('/blog/new/', methods=['GET', 'POST'])
@login_required
def new_blog():
    form = BlogForm()
    if request.method == 'POST':
        if 'description' in request.form and 'title' in request.form:
            title = form.title.data
            description = form.description.data
            owner_id = current_user.id
            blog = Blog(title=title, description=description, owner_id=owner_id)

            db.session.add(blog)
            db.session.commit()
            return redirect(url_for('main.blog', id=blog.id))
    else:
        print(request.form)
    return render_template('new-blog.html', form=form)


@main.route('/blog/edit/<int:id>/', methods=['GET', 'POST'])
@login_required
def edit_blog(id):
    blog = Blog.query.get(id)
    if request.method == 'POST':
        if 'description' in request.form and 'title' in request.form:
            title = request.form['title']
            description = request.form['description']
            blog.title = title
            blog.description=description
            db.session.add(blog)
            db.session.commit()
            return redirect(url_for('main.blog', id=blog.id))
    else:
        print(request.form)
    return render_template('edit-blog.html', blog=blog)


@main.route('/blog/<int:id>/', methods=['GET', 'POST'])
def blog(id):
    blog = Blog.query.get(id)
    comment_form = CommentForm()

    comments = Comment.query.filter_by(blog_id=blog.id)

    if request.method == 'POST':
        if 'description' in request.form:
            description = comment_form.description.data
            user_id = current_user.id
            comment = Comment(description=description, user_id=user_id, blog_id=blog.id)
            db.session.add(comment)
            db.session.commit()
            return redirect(url_for('main.blog', id=blog.id))

        if 'comment_id' in request.form:
            comment_id = request.form['comment_id']
            comment = Comment.query.get(int(comment_id))
            db.session.delete(comment)
            db.session.commit()
            return redirect(url_for('main.blog', id=blog.id))

        if 'delete_blog' in request.form:
            db.session.delete(blog)
            db.session.commit()
            return redirect(url_for('main.all_blogs'))

    return render_template('blog.html', blog=blog, comment_form=comment_form, comments=comments)
