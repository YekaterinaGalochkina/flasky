from flask import Blueprint, abort, make_response, request, Response
from app.models.dog import Dog
from ..db import db
from .route_utilities import validate_model

bp = Blueprint("dogs_bp", __name__, url_prefix = "/dogs")

@bp.post("")
def create_dog():
    request_body = request.get_json()
    new_dog = Dog.from_dict(request_body)
    
    db.session.add(new_dog)
    db.session.commit()

    return new_dog.to_dict(), 201

@bp.get("")
def get_all_dogs():
    query = db.select(Dog)

    name_param = request.args.get("name")
    if name_param:
        query = db.select(Dog).where(Dog.name.ilike(f"{name_param}"))

    color_param = request.args.get("color")    
    if color_param:
        query = db.select(Dog).where(Dog.color.ilike(f"%{color_param}"))


    # Add sorting by attribute if 'sort' param exists
    sort_param = request.args.get("sort")
    if sort_param:
        if sort_param == "name":
            query = query.order_by(Dog.name)
        elif sort_param == "color":
            query = query.order_by(Dog.color)
        elif sort_param == "temperament":
            query = query.order_by(Dog.temperament)
        elif sort_param == "is_vaccinated":
            query = query.order_by(Dog.is_vaccinated)

    dogs = db.session.scalars(query)

    dogs_response = []
    for dog in dogs:
        dogs_response.append(dog.to_dict())
    return dogs_response


@bp.get("/<id>")
def get_one_dog(id):
    dog = validate_model(Dog,id)
    return dog.to_dict()


@bp.put("/<id>")
def update_dog(id):
    dog = validate_model(Dog, id)
    request_body = request.get_json()

    dog.name = request_body["name"]
    dog.color = request_body["color"]
    dog.temperament = request_body["temperament"]
    dog.is_vaccinated = request_body["is_vaccinated"]

    db.session.commit()

    return Response(status=204, mimetype="application/json")


@bp.delete("/<id>")
def delete_dog(id):
    dog = validate_model(Dog, id)
    db.session.delete(dog)
    db.session.commit()

    return Response(status=204, mimetype="application/json")

@bp.delete("")
def delete_all_dogs():
    dogs = db.session.scalars(db.select(Dog)).all()
    
    for dog in dogs:
        db.session.delete(dog)
    
    db.session.commit()
    
    return {"message": f"Deleted {len(dogs)} dogs."}, 200


