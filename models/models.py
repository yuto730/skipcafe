from database import db, UserMixin

class Contact(db.Model):
    __tablename__ = 'contacts'
    id                = db.Column(db.Integer, primary_key=True)
    name              = db.Column(db.String(30), nullable=True)
    url               = db.Column(db.Text)
    mail              = db.Column(db.String(300), nullable=True)
    mail_confirmation = db.Column(db.String(300), nullable=True)
    message           = db.Column(db.Text, nullable=True)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id                    = db.Column(db.Integer, primary_key=True)
    user_name             = db.Column(db.String(30), nullable=True, unique=True)
    email                 = db.Column(db.String(300), nullable=True, unique=True)
    password              = db.Column(db.String(300), nullable=True)
    password_confirmation = db.Column(db.String(300), nullable=True)
    first_name            = db.Column(db.String(30), nullable=True)
    last_name             = db.Column(db.String(30), nullable=True)