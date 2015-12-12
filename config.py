import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = '2LVjegCxwzm0NvUJ'
UPLOAD_FOLDER = os.path.join(basedir, 'app', 'static', 'uploads')
AVATAR_UPLOAD_FOLDER = os.path.join(UPLOAD_FOLDER, 'avatars')
TOUR_IMAGES_UPLOAD_FOLDER = os.path.join(UPLOAD_FOLDER, 'tour-images')

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'orbi0101@gmail.com'
MAIL_PASSWORD = ''
