from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.databases.db import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    
    name: Mapped[str]
    email: Mapped[str] = mapped_column(index=True, unique=True)
    password: Mapped[str]
    # age: Mapped[int | None] = mapped_column(default=None)
    phone: Mapped[str | None]
    telegram: Mapped[str | None]
    share_contacts: Mapped[bool] = True

