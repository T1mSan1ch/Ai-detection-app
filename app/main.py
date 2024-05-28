from fastapi import FastAPI
import logging

from app.users.router import router as router_users
from app.checks.router import router as router_checks
from app.inference.predictions import router as router_predict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Сервис для проверки изображения на deepfake",
    tags=["Проверка изображений"]
)

app.include_router(router_users)
app.include_router(router_checks)
app.include_router(router_predict)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
