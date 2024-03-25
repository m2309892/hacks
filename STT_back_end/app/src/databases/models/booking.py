from datetime import datetime

from sqlalchemy import ForeignKey, DateTime, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.schemas.autotrack import FilterEngine, FilterWeelDrive
from src.databases.db import Base
from src.databases.models.users import User
from src.databases.models.autotrack import Autotrack

class Booking(Base):
    __tablename__ = 'booking'
    
    id: Mapped[int] = mapped_column(primary_key = True, index=True)
    
    subject_id: Mapped[int] = mapped_column(ForeignKey('tracks.id', ondelete='CASCADE'))
    subject: Mapped[Autotrack] = relationship(uselist=True, lazy='immediate')
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    user: Mapped[User] = relationship(uselist=False, lazy='immediate')
    # related_booking_id: Mapped[int] = mapped_column(ForeignKey('booking.id'), nullable=True, default=None)
    # related_booking: Mapped['Booking'] = relationship(uselist=False)
    # created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    data_start: Mapped[TIMESTAMP] = mapped_column(default = None)
    data_end: Mapped[TIMESTAMP] = mapped_column(default = None)
    status: Mapped[bool] = mapped_column(default=True)
    