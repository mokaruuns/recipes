import time
from typing import List
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from config import REDIS_HOST, REDIS_PORT

from fastapi import FastAPI, Query, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from models.models import Ingredient as model_ingredient
from schemas import Ingredient as schemas_ingredient
from redis import asyncio as aioredis
from math import factorial

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


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


@app.get("/fact{number}")
@cache(expire=60)
async def fact(number: int):
    time.sleep(2)
    return factorial(number)
