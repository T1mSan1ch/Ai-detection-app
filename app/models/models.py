from sqlalchemy import String, Integer, Column, Boolean, JSON
from app.database import Base


class Models(Base):
    __tablename__ = 'models'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    num_param = Column(Integer, nullable=True)
    path = Column(String, nullable=False)
    location = Column(Boolean, nullable=False)
    config = Column(JSON, nullable=False)
