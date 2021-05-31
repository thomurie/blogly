"""Blogly application."""

from flask import Flask, render_template, request, redirect
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.init(app)
db.create_all()

@app.route('/', methods=["GET"] )
def home():
    return redirect('/users')

@app.route('/users', methods=["GET"] )
def home():
    users = User.query.all()
    # links to users/new
    return render_template('index.html', users = users)

@app.route('/users/new', methods=["GET"] )
def home():
    return render_template('form.html')

@app.route('/users/new', methods=["POST"] )
def home():
   return redirect('/users')

@app.route('/users/<int:user_id>', methods=["GET"] )
def home(user_id):
    user = User.query.filter(User.id == user_id)
    # link to /users/<int:user_id>/edit
    # link to /users/<int:user_id>/delete
    return render_template('user.html', user = user)

@app.route('/users/<int:user_id>/edit', methods=["GET"] )
def home(user_id):
    user = User.query.filter(User.id == user_id)
    # link to cancel, returns to userpagwe
    return render_template('edit.html', user = user)

@app.route('/users/<int:user_id>/edit', methods=["POST"] )
def home(user_id):
    return redirect('/users')

@app.route('/users/<int:user_id>/delete', methods=["POST"] )
def home(user_id):
    return redirect('/users')