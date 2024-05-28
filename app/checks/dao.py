from app.dao.base import BaseDAO
from app.checks.models import Checks


class CheckDAO(BaseDAO):
    model = Checks
