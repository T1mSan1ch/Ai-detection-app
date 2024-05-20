from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse

from pathlib import Path
from PIL import Image
import io

from app.inference import Inference

app = FastAPI()

IMAGES_DIR = Path("../temp_img_storage")
IMAGES_DIR.mkdir(exist_ok=True)

inference_model = Inference()


@app.post("/predict/")
async def predict_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))

        # Сохранение изображения в локальной папке
        file_path = IMAGES_DIR / file.filename
        with open(file_path, "wb") as f:
            f.write(contents)

        # Получение предсказания
        probability = inference_model.predict(image)

        return JSONResponse(content={"probability": probability, "file_path": str(file_path)})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
