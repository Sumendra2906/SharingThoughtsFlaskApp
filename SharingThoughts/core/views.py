from flask import render_template, request, Blueprint, url_for
from SharingThoughts.models import User, Post

core = Blueprint('core', __name__)


@core.route('/')
def index():
    '''
    This is the home page view.
    '''
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@core.route('/about')
def info():
    '''
    Our About Page
    '''
    return render_template('about.html')

@core.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)
