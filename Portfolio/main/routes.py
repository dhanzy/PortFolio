import os

from flask import render_template, Blueprint, send_file, send_from_directory



main = Blueprint('main', __name__)


@main.route('/<filename>')
def get_static_files(filename):
    path = os.path.join('static',filename)
    return send_file(path, as_attachment=True)
    # return send_from_directory(path, filename=filename, as_attachment=True)


@main.route('/')
def index():
    return render_template('index.html')