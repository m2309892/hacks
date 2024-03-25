import aiofiles
from fastapi import UploadFile, HTTPException
from sqlalchemy import and_, select
from sqlalchemy.orm import joinedload
from starlette import status

from src.repositories.base import SQLAlchemyRepository, BaseRepository
from src.databases.models.autotrack import AutoTrack, Booking
from src.databases.db import async_session
from src.schemas.base import BaseFilterData
from src.schemas.autotrack import GetAutoTrackDTO, CreateAutoTrackDTO, UpdateAutoTrackDTO, AutoTrackFilterData
from src.services.files import download_image


class AutoTracksRepository(BaseRepository, SQLAlchemyRepository):
    model = AutoTrack
    
    async def get(self, autotrack_id: int, user_id:  int):
        async with async_session() as session:
            return await self.get_object(
                session,
                self.model.id == autotrack_id,
                GetAutoTrackDTO
            )

    async def get_all(self, limit: int = 1000, offset: int = 0, filter_data: AutoTrackFilterData | None = None):
        async with async_session() as session:
            return await self.get_objects(
                session,
                GetAutoTrackDTO,
                limit,
                offset,
                filter_data=filter_data
            )
            
    async def create(self, data: CreateAutoTrackDTO):
        async with async_session() as session:
            # new_obj = self.model(**data.model_dump())
            new_obj = self.create_object(session, data, CreateAutoTrackDTO)
            session.add(new_obj)
            await session.commit()
            await session.refresh(new_obj)