from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

db = SQLAlchemy()

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    uploaded_at = db.Column(db.DateTime, server_default=func.now())

    def __repr__(self):
        return f'<Image {self.name}>'

    def __init__(self, name: str):
        self.name = name



