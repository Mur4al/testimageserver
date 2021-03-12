import os
from pathlib import Path

from flask import Flask
from flask_migrate import Migrate
from .models import db

app = Flask(__name__)

app.secret_key = 'very_secret_key'

app.config['BASE_DIR'] = Path(__file__).parent.parent
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = os.path.join(app.config['BASE_DIR'], 'images/')

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////{app.config["BASE_DIR"]}/test.db'
db.app = app
db.init_app(app)
db.create_all()


from images_app import views
