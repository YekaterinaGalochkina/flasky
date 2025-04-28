from flask import Blueprint, abort, make_response, request, Response
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


@dogs_bp.get("/<id>")
def get_one_cat(id):
    dog = validate_dog(id)
    return {
        "id": dog.id,
        "name": dog.name,
        "color": dog.color,
        "temperament": dog.temperament
    }

def validate_dog(id):
    try:
        id = int(id)
    except ValueError:
        invalid = {"message": f"Dog id ({id}) is invalid."}
        abort(make_response(invalid, 400))

    query = db.select(Dog).where(Dog.id == id)
    dog = db.session.scalar(query)

    if not dog:
        not_found = {"message": f"Dog with id ({id}) not found."}
        abort(make_response(not_found, 404))

    return dog


@dogs_bp.put("/<id>")
def update_dog(id):
    dog = validate_dog(id)
    request_body = request.get_json()

    dog.name = request_body["name"]
    dog.color = request_body["color"]
    dog.temperament = request_body["temperament"]

    db.session.commit()

    return Response(status=204, mimetype="application/json")


@dogs_bp.delete("/<id>")
def delete_dog(id):
    dog = validate_dog(id)
    db.session.delete(dog)
    db.session.commit()

    return Response(status=204, mimetype="application/json")


