from pydantic import BaseModel


class Dish(BaseModel):
    id: int
    name: str
    url: str
    recipe: str

    class Config:
        orm_mode = True


class Ingredient(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class Person(BaseModel):
    id: int
    name: str
    email: str
    password: str
    age: int

    class Config:
        orm_mode = True
