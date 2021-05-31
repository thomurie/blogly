from models import User, db
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