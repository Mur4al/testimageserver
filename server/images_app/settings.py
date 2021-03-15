import os
from pathlib import Path


class Settings:
    SECRET_KEY = b'very_secret_key'

    BASE_DIR = Path(__file__).parent.parent
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'images/')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAX_CONTENT_LENGTH = 20 * 1024 * 1024