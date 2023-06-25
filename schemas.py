from pydantic import BaseModel


class Dish(BaseModel):
    name: str
    url: str
    recipe: str


class Ingredient(BaseModel):
    name: str


class Person(BaseModel):
    name: str
    email: str
    password: str
    age: int
