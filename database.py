from __future__ import annotations

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from config import DB_USER, DB_PORT, DB_HOST, DB_PASS, DB_NAME

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(DATABASE_URL)
async_session = AsyncSession(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session as session:
        yield session
