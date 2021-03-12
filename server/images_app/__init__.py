import os
from pathlib import Path

from flask import Flask

app = Flask(__name__)

app.secret_key = 'very_secret_key'

app.config['BASE_DIR'] = Path(__file__).parent.parent
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = os.path.join(app.config['BASE_DIR'], 'images/')



from images_app import views
