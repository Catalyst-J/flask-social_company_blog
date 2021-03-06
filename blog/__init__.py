# Holds organizational logic
# Connecting the blueprint, login_manager and others together.

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

################
# Forms
################

# This should be set in an environment variable so that it's not included in the code.
app.config['SECRET_KEY'] = 'somesupersecurekey'

################
# Database
################
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

################
# Login Configurations
################
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'


################
# View Blueprints
################

# Import the Views of 'Core' then register its blueprint.
from blog.core.views import core
app.register_blueprint(core)

# Import the error handlers.
from blog.error_pages.handlers import error_pages
app.register_blueprint(error_pages)

# Import the Views of 'Users' then register its blueprint.
from blog.users.views import users
app.register_blueprint(users)

# Import the Views of 'Blog Posts' then register its blueprint.
from blog.blog_posts.views import blog_posts
app.register_blueprint(blog_posts)