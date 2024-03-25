from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from src.databases.db import async_session


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
