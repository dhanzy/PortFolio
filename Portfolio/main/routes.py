import os

from flask import render_template, Blueprint, send_file, send_from_directory



main = Blueprint('main', __name__)



@main.route('/<filename>')
def get_static_files(filename):
    return send_from_directory('static', filename=filename, as_attachment=True)


@main.route('/')
def index():
    return render_template('index.html')