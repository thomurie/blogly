"""Blogly application."""

from flask import Flask, render_template, request, redirect
from models import db, connect_db, User, Post, Tag, PostTag

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

# PART TWO
# POST Routes

@app.route('/users/<int:user_id>/posts/new', methods =["GET"])
def get_new_user_post(user_id):
    user = User.query.filter_by(id = user_id).first()
    tags = Tag.query.all()
    return render_template('new_post.html', user = user, tags = tags)

@app.route('/users/<int:user_id>/posts/new', methods =["POST"])
def post_new_user_post(user_id):
    title = request.form.get('posttitle')
    content = request.form.get('content')

    tags =[]

    for tag in Tag.query.all():
        if request.form.get(str(tag.id)):
            tags.append(tag.id)
        else:
            None

    newpost = Post(title = title, content = content, user_id = user_id)

    db.session.add(newpost)
    db.session.commit()

    recent_post = Post.query.filter_by(id = len(Post.query.all())).first()

    for tag in tags:
        add_tag = PostTag(post_id = recent_post.id, tag_id = tag)
        db.session.add(add_tag)
        db.session.commit()

    return redirect(f"/users/{user_id}")

@app.route('/posts/<int:post_id>', methods=["GET"])
def show_post(post_id):
    post = Post.query.filter_by(id = post_id).first()
    return render_template('post.html', post = post)

@app.route('/posts/<int:post_id>/edit', methods=["GET"])
def show_edit_form(post_id):
    post = Post.query.filter_by(id = post_id).first()
    tags = Tag.query.all()
    return render_template("edit_post.html", post = post, tags = tags)

@app.route('/posts/<int:post_id>/edit', methods=["POST"])
def handle_edit_form(post_id):
    title = request.form.get('posttitle')
    content = request.form.get('content')

    post = Post.query.filter_by(id = post_id).first()

    post.title = title
    post.content = content

    db.session.add(post)
    db.session.commit()

    PostTag.query.filter_by(post_id = post_id).delete()

    tags =[]

    for tag in Tag.query.all():
        if request.form.get(str(tag.id)):
            tags.append(tag.id)
        else:
            None

    for tag in tags:
        add_tag = PostTag(post_id = post_id, tag_id = tag)
        db.session.add(add_tag)
        db.session.commit()

    return redirect(f'/posts/{post_id}')

@app.route('/posts/<int:post_id>/delete', methods = ['POST'])
def delete_post(post_id):
    Post.query.filter_by(id = post_id).delete()
    db.session.commit()
    return redirect("/users")

# PART THREE
# TAG Routes

@app.route('/tags', methods =["GET"])
def tags():
    tags = Tag.query.all()
    return render_template('all_tags.html', tags = tags)

@app.route('/tags/<int:tag_id>', methods =["GET"])
def tag_by_id(tag_id):
    tag = Tag.query.filter_by(id = tag_id).first()
    return render_template('tag.html', tag = tag)

@app.route('/tags/new', methods =["GET"])
def new_tag():
    return render_template('new_tag.html')

@app.route('/tags/new', methods =["POST"])
def post_new_tag_request():
    name = request.form.get('name')

    new_tag = Tag(name = name)

    db.session.add(new_tag)
    db.session.commit()

    return redirect('/tags')


@app.route('/tags/<int:tag_id>/edit', methods =["GET"])
def edit_tag_form(tag_id):
    tag = Tag.query.filter_by(id = tag_id).first()
    return render_template('edit_tag.html', tag = tag)

@app.route('/tags/<int:tag_id>/edit', methods =["POST"])
def post_changes_to_tag(tag_id):
    name = request.form.get('name')
    tag = Tag.query.filter_by(id = tag_id).first()

    tag.name = name

    db.session.add(tag)
    db.session.commit()

    return redirect('/tags')

@app.route('/tags/<int:tag_id>/delete', methods =["POST"])
def remove_tag(tag_id):
    PostTag.query.filter_by(tag_id = tag_id).delete()
    Tag.query.filter_by(id = tag_id).delete()
    db.session.commit()
    return redirect('/tags')

