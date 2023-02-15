import os
from dotenv import load_dotenv
# import sys

basedir = os.path.abspath(os.path.dirname(__file__))
# basedir = sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '63ec511d7bf94c14a4e23799f3f3a8b9'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT') or 465
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ["jackkiwema@gmail.com", "ogollahyasseh@gmail.com"]
    LANGUAGES = ['en', 'es']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    POSTS_PER_PAGE = 4