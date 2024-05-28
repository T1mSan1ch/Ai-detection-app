import io
from datetime import datetime
from PIL import Image
from fastapi import Depends, APIRouter, File, UploadFile, Form
from starlette.responses import JSONResponse

from app.image_saver import generate_unique_filename
from app.inference.inference import Inference
from app.users.dependencies import get_current_user
from app.users.models import User
from app.checks.dao import CheckDAO

inference_model = Inference()

router = APIRouter(
    prefix="/predict",
    tags=["Проверка изображения"]
)


@router.post("")
async def prediction(
        file: UploadFile = File(...),
        model_id: int = Form(...),
        ai_or_real: bool = Form(...),
        user: User = Depends(get_current_user)
):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    file_path = generate_unique_filename('JPEG')
    probability = inference_model.predict(image)
    image.save(file_path, 'JPEG')

    await CheckDAO.add(
        user_id=user.id,
        result=probability,
        model_id=model_id,
        image_path=str(file_path),
        current=ai_or_real,
        date=datetime.utcnow()
    )
    return JSONResponse(
        content={"probability": probability, "file_path": str(file_path)}
    )

