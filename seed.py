from models import User, db, Post, Tag, PostTag
from app import app

db.drop_all()
db.create_all()

User.query.delete()

img = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQTZG27hsLIO0KhRtnjLKb5qEw7rduoedCMiw&usqp=CAU'

john = User(first_name = 'John', last_name = "Lennon", image_url = img)
paul = User(first_name = 'Paul', last_name = "Mcartney", image_url = img)
george = User(first_name = 'George', last_name = "Harriosn", image_url = img)
ringo = User(first_name = 'Ringo', last_name = "Starr", image_url = img)

db.session.add(john)
db.session.add(paul)
db.session.add(george)
db.session.add(ringo)

db.session.commit()

john_post_one = Post(title= 'Uno', content = 'This is my very first post', user_id = 1)
john_post_two =  Post(title= 'Two', content = 'This is my very second post', user_id = 1)
john_post_three =  Post(title= 'Tres', content = 'This is my very third post', user_id = 1)

paul_post_one = Post(title= 'Uno', content = 'This is my very first post', user_id = 2)
paul_post_two =  Post(title= 'Two', content = 'This is my very second post', user_id = 2)
paul_post_three =  Post(title= 'Tres', content = 'This is my very third post', user_id = 2)

db.session.add(john_post_one)
db.session.add(john_post_two)
db.session.add(john_post_three)

db.session.add(paul_post_one)
db.session.add(paul_post_two)
db.session.add(paul_post_three)

db.session.commit()

funny = Tag(name = 'funny')
trending = Tag(name = 'trending')
sad = Tag(name = 'sad')

db.session.add(funny)
db.session.add(trending)
db.session.add(sad)

db.session.commit()

def addtag(post_id, tag_id):
    return PostTag(post_id= post_id, tag_id = tag_id)

one_funny = addtag(1, 1)
three_trending = addtag(3,2)
four_sad = addtag(4,3)

db.session.add(one_funny)
db.session.add(three_trending)
db.session.add(four_sad)

db.session.commit()

