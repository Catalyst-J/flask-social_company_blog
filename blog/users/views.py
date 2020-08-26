
# Views:
# - Register
# - Login
# - Logout
# - Account
# - User's Blog Posts

from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required

from blog import db
from blog.models import User, BlogPost
from blog.users.forms import RegisterForm, LoginForm, UpdateUserForm
from blog.users.picture_handler import add_profile_pic

# Remember to activate the blueprint in the project's __init__.py
users = Blueprint('users', __name__)

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))

# Basic controller only
@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)

# Basic controller only
@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # Used .first() to ensure to get the right format, and not get a list/dictionary
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Log-in success!')

            # Redirector to login when it's needed in a view.
            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('core.index')

            return redirect(next)

    return render_template('login.html', form=form)

# Basic controller for updating User
@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateUserForm()

    if form.validate_on_submit():
        
        # This if-statement is triggered when a user attempts to upload a file
        if form.picture.data:
            username = current_user.username
            picture = add_profile_pic(form.picture.data, username)
            current_user.profile_img = picture

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()

        flash('User Account Updated')

        return redirect(url_for('users.account'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    profile_image = url_for('static', filename='profile_pics/' + current_user.profile_img)

    return render_template('account.html', form=form, profile_img=profile_image)

# User Profile
@users.route('/<username>')
def user_posts(username):
    
    # Grab the page itself
    # Cycle through posts in pages
    page = request.args.get('page', 1, type=int)
    
    # .first_or_404 -- returns a 404 Error if user is inexistent
    user = User.query.filter_by(username=username).first_or_404()

    # 'author' is the back reference for the User <-> BlogPost relationship
    # Paginate handles the pages, then limits the results into just 5 per page.
    # Ordered by descending order of the date.
    blog_posts = BlogPost.query.filter_by(author=user).order_by(BlogPost.data.desc()).paginate(page=page, per_page=5)

    return render_template('user_blog_posts.html', blog_posts=blog_posts, user=user)    


