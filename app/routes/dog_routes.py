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
    is_vaccinated = request_body["is_vaccinated"]

    new_dog = Dog(name=name, color=color, temperament=temperament, is_vaccinated=is_vaccinated)
    db.session.add(new_dog)
    db.session.commit()

    response = {
        "id": new_dog.id,
        "name": new_dog.name,
        "color": new_dog.color,
        "temperament": new_dog.temperament,
        "is_vaccinated": new_dog.is_vaccinated
    }
    return response, 201

@dogs_bp.get("")
def get_all_dogs():
    query = db.select(Dog)

    name_param = request.args.get("name")
    if name_param:
        query = db.select(Dog).where(Dog.name.ilike(f"{name_param}"))

    color_param = request.args.get("color")    
    if color_param:
        query = db.select(Dog).where(Dog.color.ilike(f"%{color_param}"))

    dogs = db.session.scalars(query)

    dogs_response = []
    for dog in dogs:
        dogs_response.append(
            {
                "id": dog.id,
                "name": dog.name,
                "color": dog.color,
                "temperament": dog.temperament,
                "is_vaccinated": dog.is_vaccinated
            }
        )
    return dogs_response


@dogs_bp.get("/<id>")
def get_one_dog(id):
    dog = validate_dog(id)
    return {
        "id": dog.id,
        "name": dog.name,
        "color": dog.color,
        "temperament": dog.temperament,
        "is_vaccinated": dog.is_vaccinated
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
    dog.is_vaccinated = request_body["is_vaccinated"]

    db.session.commit()

    return Response(status=204, mimetype="application/json")


@dogs_bp.delete("/<id>")
def delete_dog(id):
    dog = validate_dog(id)
    db.session.delete(dog)
    db.session.commit()

    return Response(status=204, mimetype="application/json")

@dogs_bp.delete("")
def delete_all_dogs():
    dogs = db.session.scalars(db.select(Dog)).all()
    
    for dog in dogs:
        db.session.delete(dog)
    
    db.session.commit()
    
    return {"message": f"Deleted {len(dogs)} dogs."}, 200


