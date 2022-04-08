import os

class Config():
    SECRET_KEY = secrets.SECRET_KEY
    # database
    SQLALCHEMY_DATABASE_URI = secrets.SQLALCHEMY_DATABASE_URI
    # for password reset
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = secrets.EMAIL_USER
    MAIL_PASSWORD = secrets.EMAIL_PASS
