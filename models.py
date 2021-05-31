"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
def connect_db(app):

    db.app = app
    db.init_app(app)

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = user

    id = db.Column(db.Integer, primary_key = True, autoincrement =True)

    first_name = db.Column(db.String(100), nullable = False)

    last_name = db.Column(db.String(100), nullable = False)

    image_url = db.Column(db.String(10000), nullable = True, default = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCDe5JZ_HkfuU5VFQDlF0j1jeCl-SCj_mJdA&usqp=CAU')
