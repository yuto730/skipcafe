from database import db

class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=True)
    url = db.Column(db.Text)
    mail = db.Column(db.String(300), nullable=True)
    mail_confirmation = db.Column(db.String(300), nullable=True)
    message = db.Column(db.Text, nullable=True)