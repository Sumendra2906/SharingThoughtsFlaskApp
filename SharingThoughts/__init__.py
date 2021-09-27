import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from SharingThoughts.config import Config

db = SQLAlchemy()

#encryption
bcrypt = Bcrypt()

#login manager
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

#for password reset
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    #Initializing
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    # Importing the blueprints
    from SharingThoughts.blogposts.views import blogposts
    from SharingThoughts.users.views import users
    from SharingThoughts.core.views import core
    from SharingThoughts.errors.handlers import errors
    # Register the apps
    app.register_blueprint(users)
    app.register_blueprint(blogposts)
    app.register_blueprint(core)
    app.register_blueprint(errors)
    return app