import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Th1sIsTh3K3yT0Succ3ss'
    SECURITY_PASSWORD_SALT = 'ss3ccuSS4ltySa1t'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://') \
                              if os.environ.get('DATABASE_URL') \
                              else 'sqlite:///' + os.path.join(basedir, 'library_app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 5
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    # MAIL_USERNAME = os.environ.get('EMAIL_USER')
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
    MAIL_SENDER = 'dbetancur@consolesolutions.net'
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
