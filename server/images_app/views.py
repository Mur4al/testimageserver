import os

from flask import request, render_template, send_from_directory, url_for
from werkzeug.exceptions import RequestEntityTooLarge

from images_app import app
from images_app.utils import is_image, save_file

from images_app.models import Image, db


@app.route('/')
def home():
    return render_template('home.html', images = Image.query.all())


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        try:
            if 'file' not in request.files:
                return {'message': 'Файл не отправлен'}, 400

            file = request.files['file']
            if file and is_image(file.filename):
                saved_file_name = save_file(file)
                image = Image(name=saved_file_name)
                db.session.add(image)
                db.session.commit()
                return {'message': 'Файл сохранен', 'address': url_for('uploaded_image', filename=saved_file_name)}, 200
            else:
                return {'message': 'Некорректный файл'}, 400
        except RequestEntityTooLarge:
            return {'message': 'Размер файла превышает установленное ограничение'}, 413

    return render_template('upload.html')


@app.route('/images/<filename>')
def uploaded_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
