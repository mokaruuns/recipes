from typing import List

from fastapi import FastAPI, Query, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from models.models import Ingredient as model_ingredient
from schemas import Ingredient as schemas_ingredient

app = FastAPI()


@app.get('/')
def home():
    return {"key": "value"}


@app.get("/kms")
async def get_specific_operations(session: AsyncSession = Depends(get_async_session)):
    query = select(model_ingredient)
    result = await session.execute(query)
    return result.scalars().all()

@app.post("/")
async def add_specific_operations(ingredient: schemas_ingredient,
                                  session: AsyncSession = Depends(get_async_session)):
    stmt = insert(model_ingredient).values(**ingredient.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
