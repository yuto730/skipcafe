from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user

db = SQLAlchemy()
login_manager = LoginManager()

def init_db(app):
    db.init_app(app)
    login_manager.init_app(app)