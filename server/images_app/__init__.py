from flask import Flask
from flask_migrate import Migrate
from .models import db
from .settings import Settings

app = Flask(__name__)
app.config.from_object(Settings)
app.secret_key = 'very_secret_key'

db.app = app
db.init_app(app)

migrate = Migrate(app,db)


from images_app import views
