from app import create_app, db
from app.models.cat import Cat
from app.models.dog import Dog

my_app = create_app()
with my_app.app_context():
    db.session.add(Cat(name="Luna", color="ash", personality="Tomato Queen")),
    db.session.add(Cat(name="Simon", color="black", personality="might be a human stuck in a cats body")),
    db.session.add(Cat(name="Midnight", color="black", personality="skittish")),
    db.session.add(Cat(name="Leo", color="gray tabby", personality="friendly")),
    db.session.add(Cat(name="Ash", color="gray", personality="cranky")),
    db.session.add(Cat(name="Alder", color="auburn", personality="bouncy, trouncy, flouncy, pouncy, fun, fun, fun, fun, fun")),
    db.session.add(Cat(name="Morty", color="orange", personality="orange")),
    db.session.add(Cat(name="fluffy", color="white", personality="evil with a hint of benevolent")),
    db.session.add(Cat(name="Reginold", color="orange", personality="only has one brain cell, but is descendent of Reginold the Great Tabby")),
    db.session.add(Cat(name="Katosa", color="gray tabby", personality="Crazy Hunter")),
    db.session.add(Cat(name="Milly", color="Tortoiseshell", personality="Loves you a lot but will probably sneeze all over you")),
    db.session.add(Cat(name="Meryl", color="Tortoiseshell", personality="Bossy but tries to pass as the sweet one")),
    db.session.add(Cat(name="Zelda", color="white, gray", personality="a mystery")),
    db.session.add(Cat(name="Jupiter", color="orange", personality="socially selective")),
    db.session.add(Cat(name="Neo", color="black", personality="stoic")),
    db.session.add(Cat(name="Gato", color="grey", personality="fun")),
    db.session.add(Cat(name="Red XIII", color="red", personality="serious")),
    db.session.add(Cat(name="Gizzy", color="white", personality="unbothered")),
    db.session.commit()

with my_app.app_context():
    db.session.add(Dog(name="Buddy", color="brown", temperament="friendly", is_vaccinated=True))
    db.session.add(Dog(name="Max", color="black", temperament="playful", is_vaccinated=True))
    db.session.add(Dog(name="Bella", color="golden", temperament="loyal", is_vaccinated=True))
    db.session.add(Dog(name="Charlie", color="white", temperament="energetic", is_vaccinated=False))
    db.session.add(Dog(name="Milo", color="beige", temperament="curious", is_vaccinated=True))
    db.session.add(Dog(name="Rocky", color="gray", temperament="adventurous", is_vaccinated=False))
    db.session.add(Dog(name="Lucy", color="tan", temperament="affectionate", is_vaccinated=True))
    db.session.add(Dog(name="Daisy", color="yellow", temperament="obedient", is_vaccinated=False))
    db.session.add(Dog(name="Sadie", color="black and white", temperament="sassy", is_vaccinated=True))
    db.session.add(Dog(name="Cooper", color="brown and white", temperament="calm", is_vaccinated=True))
    db.session.add(Dog(name="Bailey", color="red", temperament="social", is_vaccinated=False))
    db.session.add(Dog(name="Jack", color="blue", temperament="mellow", is_vaccinated=True))
    db.session.add(Dog(name="Lola", color="spotted", temperament="cheerful", is_vaccinated=True))
    db.session.add(Dog(name="Chester", color="gray and white", temperament="mischievous", is_vaccinated=False))
    db.session.add(Dog(name="Penny", color="chocolate", temperament="sweet", is_vaccinated=True))
    db.session.add(Dog(name="Rex", color="black", temperament="protective", is_vaccinated=True))
    db.session.add(Dog(name="Toby", color="brown", temperament="easygoing", is_vaccinated=False))
    db.session.add(Dog(name="Sophie", color="cream", temperament="energetic", is_vaccinated=True))
    db.session.add(Dog(name="Ziggy", color="silver", temperament="loving", is_vaccinated=True))
    db.session.commit()