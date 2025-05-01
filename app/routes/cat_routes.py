from flask import Blueprint, abort, make_response, request, Response
from app.models.cat import Cat
from ..db import db

cats_bp = Blueprint("cats_bp", __name__, url_prefix = "/cats")

@cats_bp.post("")
def create_cat():
    request_body = request.get_json()
    name = request_body["name"]
    color = request_body["color"]
    personality = request_body["personality"]

    new_cat = Cat(name=name, color=color, personality=personality)
    db.session.add(new_cat)
    db.session.commit()

    return new_cat.to_dict(), 201

@cats_bp.get("")
def get_all_cats():
    query = db.select(Cat)

    name_param = request.args.get("name")
    if name_param:
        query = db.select(Cat).where(Cat.name == name_param)

    color_param = request.args.get("color")    
    if color_param:
        query = query.where(Cat.color.ilike(f"%{color_param}%"))
    
    query = query.order_by(Cat.name)

    cats = db.session.scalars(query)

    cats_response = []
    for cat in cats: 
        cats_response.append(cat.to_dict())

    return cats_response

@cats_bp.get("/<id>")
def get_one_cat(id):
    cat = validate_cat(id)
    return cat.to_dict()

def validate_cat(id):
    try:
        id = int(id)
    except ValueError:
        invalid = {"message": f"Cat id ({id}) is invalid."}
        abort(make_response(invalid, 400))

    query = db.select(Cat).where(Cat.id == id)
    cat = db.session.scalar(query)

    if not cat:
        not_found = {"message": f"Cat with id ({id}) not found."}
        abort(make_response(not_found, 404))

    return cat

@cats_bp.put("/<id>")
def update_cat(id):
    cat = validate_cat(id)
    request_body = request.get_json()

    cat.name = request_body["name"]
    cat.color = request_body["color"]
    cat.personality = request_body["personality"]

    db.session.commit()

    return Response(status=204, mimetype="application/json")


@cats_bp.delete("/<id>")
def delete_cat(id):
    cat = validate_cat(id)
    db.session.delete(cat)
    db.session.commit()

    return Response(status=204, mimetype="application/json")

@cats_bp.delete("")
def delete_all_cats():
    cats = db.session.scalars(db.select(Cat)).all()
    
    for cat in cats:
        db.session.delete(cat)
    
    db.session.commit()
    
    return {"message": f"Deleted {len(cats)} cats."}, 200







