import pytest
from app import create_app
from app.db import db
from flask.signals import request_finished
from dotenv import load_dotenv
import os
from app.models.cat import Cat
from app.models.dog import Dog

load_dotenv()

@pytest.fixture
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }
    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def two_saved_cats(app):
    # Arrange
    ocean_cat = Cat(name="Ocean",
                    personality="brave",
                    color="blue")
    mountain_cat = Cat(name="Mountain",
                        personality="rocky",
                        color="red")

    db.session.add_all([ocean_cat, mountain_cat])
    db.session.commit()

@pytest.fixture
def two_saved_dogs(app):
    # Arrange
    ocean_dog = Dog(name="Ocean",
                    temperament="brave",
                    color="blue",
                    is_vaccinated=False)
    mountain_dog = Dog(name="Mountain",
                        temperament="rocky",
                        color="red",
                        is_vaccinated=True)

    db.session.add_all([ocean_dog, mountain_dog])
    db.session.commit()