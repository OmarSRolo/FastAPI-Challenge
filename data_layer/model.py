from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, Boolean, String

from .dbcontext import Base


class JokeModel(Base):
    __tablename__ = "pref_joke"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    is_active = Column(Boolean, default=False, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    text = Column(String, nullable=False)
