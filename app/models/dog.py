from sqlalchemy.orm import Mapped, mapped_column
from ..db import db


class Dog(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    color: Mapped[str]
    temperament: Mapped[str]


# class Dog:
#     def __init__(self, id, name, color, temperament):
#         self.id = id
#         self.name = name
#         self.color = color
#         self.temperament = temperament

# dogs = [
#     Dog(1, "Rex", "brown", "loyal"),
#     Dog(2, "Bella", "black", "playful"),
#     Dog(3, "Max", "white", "calm"),
#     Dog(4, "Mils", "golden", "friendly")
# ]

