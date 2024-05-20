from sqlalchemy import Integer, Column, ForeignKey, Float, String, Boolean
from app.database import Base


class Checks(Base):
    __tablename__ = 'checks'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    result = Column(Float, nullable=False)
    model_id = Column(Integer, ForeignKey('models.id'))
    image_path = Column(String, nullable=False)
    current = Column(Boolean, nullable=False)
