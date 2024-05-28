from pydantic import BaseModel
from datetime import datetime


class SChecks(BaseModel):
    id: int
    user_id: int
    result: int
    date: datetime
    model_id: int
    image_path: str
    current: bool

    class Config:
        from_attributes = True

