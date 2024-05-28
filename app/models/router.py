from fastapi import APIRouter
from dao import ModelsDAO

router = APIRouter(
    prefix="/models",
    tags=["Получение моделей проверки изображения"]
)


@router.get("")
async def get_checks():
    return await ModelsDAO.find_one_or_none(0)