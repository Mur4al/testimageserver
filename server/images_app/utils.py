import os
import uuid
from typing import Optional

from werkzeug.utils import secure_filename

from images_app import app

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def is_image(filename):
    # Пропустит неверные файлы с правильным расширением
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_image_ext(filename: str) -> Optional[str]:
    return filename.rsplit('.', 1)[1].lower()


def unique_filename(ext: str) -> str:
    return f'{str(uuid.uuid4().hex)}.{ext}'


def save_file(file) -> str:
    ext = get_image_ext(secure_filename(file.filename))
    filename = unique_filename(ext)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return filename
