"""Blogly application."""

from flask import Flask, render_template, request, redirect
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

@app.route('/', methods=["GET"])
def home_page():
    return redirect('/users')

@app.route('/users', methods=["GET"] )
def users():
    users = User.query.all()
    # links to users/new
    return render_template('index.html', users = users)

@app.route('/users/new', methods=["GET"] )
def new_get():
    return render_template('form.html')

@app.route('/users/new', methods=["POST"] )
def new_post():
    fname = request.form.get('firstname')
    lname = request.form.get('lastname')
    imgurl = request.form.get('imageurl')
    newuser = User(first_name = fname, last_name = lname, image_url = imgurl)
    db.session.add(newuser)
    db.session.commit()
    return redirect('/users')

@app.route('/users/<int:user_id>', methods=["GET"] )
def user_by_id(user_id):
    user = User.query.filter_by(id = user_id).first()
    return render_template('user.html', user = user)

@app.route('/users/<int:user_id>/edit', methods=["GET"] )
def edit_user(user_id):
    user = User.query.filter_by(id = user_id).first()
    return render_template('edit.html', user = user)

@app.route('/users/<int:user_id>/edit', methods=["POST"] )
def edit_user_post(user_id):
    fname = request.form.get('firstname')
    lname = request.form.get('lastname')
    imgurl = request.form.get('imageurl')
    user = User.query.filter_by(id = user_id).first()
    user.first_name = fname
    user.last_name = lname
    user.image_url = imgurl
    db.session.add(user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>/delete', methods=["POST"] )
def delete_user(user_id):
    User.query.filter_by(id = user_id).delete()
    db.session.commit()
    return redirect('/users')