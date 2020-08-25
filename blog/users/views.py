
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
    login_user()
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





