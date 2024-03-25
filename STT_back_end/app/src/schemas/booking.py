
from sqlalchemy import TIMESTAMP
from pydantic import BaseModel
from src.schemas.base import BaseFilterData
from src.schemas.autotrack import GetAutoTrackDTO
from src.databases.models.autotrack import Autotrack
from src.databases.models.users import User

class GetBookingDTO(BaseModel):
    id: int
    subject: Autotrack
    user: User
    data_start: TIMESTAMP
    data_end: TIMESTAMP
    status: bool
    
class CreateBookingDTO(BaseModel):
    subject_id: int
    user_id: int
    data_start: TIMESTAMP
    data_end: TIMESTAMP
    status: bool


class UpdateBookingDTO(BaseModel):
    status: bool


class BookingFilterData(BaseFilterData):
    status: bool | None = None
