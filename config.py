import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Th1sIsTh3K3yT0Succ3ss'
    SECURITY_PASSWORD_SALT = 'ss3ccuSS4ltySa1t'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://') \
                              or 'sqlite:///' + os.path.join(basedir, 'library_app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'localhost'
    MAIL_PORT = '8025'
    MAIL_SENDER = 'dbetancur@consolesolutions.net'
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
