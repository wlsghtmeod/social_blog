from flask import render_template, request, Blueprint
from flask_login import current_user
from socialblog.models import BlogPost,User

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page',1,type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page,per_page=5)
    return render_template('index.html',blog_posts=blog_posts)

@core.route('/dashboard')
def dashboard():
    page = request.args.get('page', 1, type=int)
    user = current_user
    blog_posts = BlogPost.query.filter_by(author=user).order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)
    return render_template('user_blog_posts.html', blog_posts=blog_posts, user=user)

@core.route('/info')
def info():
    return render_template('info.html')