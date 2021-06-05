"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
import datetime

def connect_db(app):

    db.app = app
    db.init_app(app)

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key = True, autoincrement =True)

    first_name = db.Column(db.String(100), nullable = False)

    last_name = db.Column(db.String(100), nullable = False)

    image_url = db.Column(db.String(10000), nullable = True, default = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCDe5JZ_HkfuU5VFQDlF0j1jeCl-SCj_mJdA&usqp=CAU')

    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")

class Post(db.Model):

    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    title = db.Column(db.Text, nullable = True)

    content = db.Column(db.Text, nullable = False)

    created_at = db.Column(db.DateTime(timezone = True), default = datetime.datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Tag(db.Model):

    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    name = db.Column(db.Text, nullable = False, unique = True)

    posts = db.relationship('Post', secondary = 'posttag', backref='all_tags')

class PostTag(db.Model):

    __tablename__ = 'posttag'

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), primary_key = True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), primary_key = True)

