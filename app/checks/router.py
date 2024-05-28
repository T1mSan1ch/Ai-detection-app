from fastapi import APIRouter, Request, Depends
from app.checks.dao import CheckDAO
from app.checks.schemas import SChecks
from app.users.models import User
from app.users.dependencies import (
    get_current_user,
    get_current_admin_user)

router = APIRouter(
    prefix="/checks",
    tags=["Проверенные изображения"]
)
@router.get("")
async def get_checks(
        user: User = Depends(get_current_user)
) -> list[SChecks]:
    return await CheckDAO.find_all(user_id=user.id)

@router.post("")
async def add_check(user: User = Depends(get_current_user)):
    await CheckDAO.add(user_id=user.id, )

@router.get("/all")
async def get_checks(
        user: User = Depends(get_current_admin_user)
) -> list[SChecks]:
    return await CheckDAO.find_all()
