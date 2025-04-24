from flask import Blueprint, abort, make_response, request
from app.models.cat import Cat
from ..db import db
# from ..models.cat import cats

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

    response = {
        "id": new_cat.id,
        "name": new_cat.name,
        "color": new_cat.color,
        "personality": new_cat.personality
    }
    return response, 201

@cats_bp.get("")
def get_all_cats():
    query = db.select(Cat).order_by(Cat.id)
    cats = db.session.scalars(query)

    cats_responce = []
    for cat in cats:
        cats_responce.append(
            {
                "id": cat.id,
                "name": cat.name,
                "color": cat.color,
                "personality": cat.personality
            }
        )
    return cats_responce


# @cats_bp.get("")
# def get_all_cats():
#     results_list = []

#     for cat in cats:
#         results_list.append(dict(
#             id = cat.id,
#             name = cat.name,
#             color = cat.color,
#             personality = cat.personality
#         ))
#     return results_list


# @cats_bp.get("/<id>")
# def get_one_cat(id):
#     cat = validate_cat(id)
#     cat_dict = dict(
#         id = cat.id,
#         name = cat.name,
#         color= cat.color,
#         personality = cat.personality
#     )
    
#     return cat_dict

# def validate_cat(id):
#     try:
#         id = int(id)
#     except ValueError:
#         invalid = {"message": f"Cat id ({id}) is invalid."}
#         abort(make_response(invalid, 400))

#     for cat in cats:
#         if cat.id == id:
#             return cat 
    
#     not_found = {"message": f"Cat with id ({id}) not found."}
#     abort(make_response(not_found, 404))