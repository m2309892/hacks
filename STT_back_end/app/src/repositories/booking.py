import aiofiles
from fastapi import UploadFile, HTTPException
from sqlalchemy import and_, select
from sqlalchemy.orm import joinedload
from starlette import status

from src.repositories.base import SQLAlchemyRepository, BaseRepository
from src.databases.models.autotrack import AutoTrack
from src.databases.models.booking import Booking
from src.databases.db import async_session
from src.schemas.base import BaseFilterData
from src.schemas.autotrack import GetAutoTrackDTO, CreateAutoTrackDTO, UpdateAutoTrackDTO, AutoTrackFilterData
from src.schemas.booking import GetBookingDTO, CreateBookingDTO, BookingFilterData, UpdateBookingDTO
from src.services.files import download_image

class BookingRepository(BaseRepository, SQLAlchemyRepository):
    model = Booking

    async def get(self, booking_id: int) -> GetBookingDTO | None:
        async with async_session() as session:
            return await self.get_object(
                session,
                and_(self.model.id == booking_id),
                GetBookingDTO,
                (joinedload(self.model.subject), joinedload(self.model.user))
            )

    async def get_all(self, limit: int = 100, offset: int = 0) -> list[GetBookingDTO]:
        async with async_session() as session:
            return await self.get_objects(
                session,
                GetBookingDTO,
                limit,
                offset,
                (joinedload(self.model.subject), joinedload(self.model.user))
            )

    async def create(self, data: CreateBookingDTO) -> GetBookingDTO | None:
        async with async_session() as session:
            self.validate_booking(session, self.model(data))
            return self.create_object(session, GetBookingDTO, data)

    async def update(self, booking_id: int, data: UpdateBookingDTO) -> None:
        async with async_session() as session:
            await self.update_object(
                session,
                data,
                and_(Booking.id == booking_id)
            )

    async def delete(self, booking_id: int) -> None:
        async with async_session() as session:
            await self.delete_object(
                session,
                and_(Booking.id == booking_id)
            )
    async def validate_booking(session, data: GetBookingDTO) -> None:
        query = (
        select(Booking)
        .where(Booking.subject_id==data.subject_id)
        .where(or_(Booking.data_start.between(data.data_start, data.data_end), Booking.data_end.between(data.data_start, data.data_end)))
        )
        rez = await session.execute(query)

        if rez.scalars().all():
            raise HTTPException(status.HTTP_400_BAD_REQUEST, 'Бронь недоступна')
