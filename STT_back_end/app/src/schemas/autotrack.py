from datetime import datetime

from sqlalchemy import TIMESTAMP
from fastapi import UploadFile
from fastapi.params import Form, File
from pydantic import BaseModel
from enum import Enum
from .base import BaseFilterData


class FilterEngine(str, Enum):
    DIEZEL = 'дизель'
    PETROL = 'бензин'
    PETROLCNG = 'гибрид(бензин/CNG)'
    PETROLLPG = 'гибрид(бензин/LPG)'

class FilterWeelDrive(str, Enum):
    FRONT_WEEL = 'front-weel drive'
    REAR_WEEL = 'rear-weel drive'
    ALL_WEEL = 'all-weel drive'


class CreateAutoTrackDTO(BaseModel):
    name: str
    price: int
    sleep_places: int
    passengers: int
    shower: bool
    engine_type: FilterEngine 
    driver_license: str
    drive_type: FilterWeelDrive
    location: str


class GetAutoTrackDTO(CreateAutoTrackDTO):
    id: int
    name: str

class AutoTrackFilterData(BaseFilterData):
    price: int | None = None
    sleep_places: int | None = None
    passengers: int | None = None
    shower: bool | None = None
    engine_type: FilterEngine | None = None
    driver_license: str | None = None
    drive_type: FilterWeelDrive | None = None
