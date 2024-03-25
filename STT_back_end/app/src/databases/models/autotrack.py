from datetime import datetime

from sqlalchemy import ForeignKey, DateTime, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.src.schemas.autotrack import FilterEngine, FilterWeelDrive
from ..db import Base
from app.src.databases.models.users import User


class Autotrack(Base):
    __tablename__ = 'tracks'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    # user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    # user: Mapped['User'] = relationship(back_populates='tracks', uselist=False)

    name: Mapped[str]
    price: Mapped[int] 
    # = Field(ge=0)
    sleep_places: Mapped[int]
    passengers: Mapped[int]
    shower: Mapped[bool]
    engine_type: Mapped[FilterEngine] 
    driver_license: Mapped[str]
    drive_type: Mapped[FilterWeelDrive]
    location: Mapped[str]
    toilet: Mapped[bool]
    description: Mapped[str]
    # photo: