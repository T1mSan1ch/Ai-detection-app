from pathlib import Path
import uuid

IMAGES_DIR = Path("temp_img_storage")


def generate_unique_filename(extension) -> Path:
    while True:

        unique_name = str(uuid.uuid4())
        unique_filename = f"{unique_name}.{extension}"
        # Проверка, существует ли уже файл с таким именем
        file_path = IMAGES_DIR / unique_filename
        if not file_path.exists():
            return file_path
