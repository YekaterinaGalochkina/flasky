from flask import Blueprint, abort, make_response, request
from app.models.dog import Dog
from ..db import db

dogs_bp = Blueprint("dogs_bp", __name__, url_prefix = "/dogs")

@dogs_bp.post("")
def create_dog():
    request_body = request.get_json()
    name = request_body["name"]
    color = request_body["color"]
    temperament = request_body["temperament"]

    new_dog = Dog(name=name, color=color, temperament=temperament)
    db.session.add(new_dog)
    db.session.commit()

    response = {
        "id": new_dog.id,
        "name": new_dog.name,
        "color": new_dog.color,
        "temperament": new_dog.temperament
    }
    return response, 201

@dogs_bp.get("")
def get_all_dogs():
    query = db.select(Dog).order_by(Dog.id)
    dogs = db.session.scalars(query)

    dogs_responce = []
    for dog in dogs:
        dogs_responce.append(
            {
                "id": dog.id,
                "name": dog.name,
                "color": dog.color,
                "temperament": dog.temperament
            }
        )
    return dogs_responce
