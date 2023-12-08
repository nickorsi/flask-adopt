from app import db, Pet

db.drop_all()
db.create_all()


pet = Pet(
    name="Woofly",
    species='dog',
    photo_url='https://i.ytimg.com/vi/SfLV8hD7zX4/maxresdefault.jpg',
    age='baby',
    available=True
)

db.session.add(pet)
db.session.commit()

pet_2 = Pet(
    name="Woofly 2",
    species='dog',
    photo_url='https://i.ytimg.com/vi/SfLV8hD7zX4/maxresdefault.jpg',
    age='adult',
    available=True
)

db.session.add(pet_2)
db.session.commit()