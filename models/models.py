from __future__ import annotations

from typing import List
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


dish_ingredient = Table(
    "dish_ingredient",
    Base.metadata,
    Column("dish_id", ForeignKey("dishes.id")),
    Column("ingredient_id", ForeignKey("ingredients.id")),
)


class Dish(Base):
    __tablename__ = "dishes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(index=True)
    url: Mapped[str] = mapped_column(unique=True)
    recipe: Mapped[str] = mapped_column()
    ingredients: Mapped[List[Ingredient]] = relationship(
        secondary=dish_ingredient, back_populates="dishes"
    )


class Ingredient(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(index=True)
    dishes: Mapped[List[Dish]] = relationship(
        secondary=dish_ingredient, back_populates="ingredients"
    )
