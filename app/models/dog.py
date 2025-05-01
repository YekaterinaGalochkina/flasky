from sqlalchemy.orm import Mapped, mapped_column
from ..db import db
from sqlalchemy import Boolean


class Dog(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    color: Mapped[str]
    temperament: Mapped[str]
    is_vaccinated: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "color": self.color,
            "temperament": self.temperament,
            "is_vaccinated": self.is_vaccinated
        }

    @classmethod
    def from_dict(cls, dog_data):
        return cls(
            name = dog_data["name"],
            color = dog_data["color"],
            temperament = dog_data["temperament"],
            is_vaccinated = dog_data["is_vaccinated"]
        )