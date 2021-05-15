import os

from flask import render_template, Blueprint, send_file, send_from_directory



main = Blueprint('main', __name__)


@main.route('/manifest.webmanifest')
def webmanifest():
    path = r'static\manifest.webmanifest'
    return send_file(path, as_attachment=True)



@main.route('/<filename>')
def resume(filename):
    path = r'static'
    if not os.path.exists(os.path.join(path, filename)):
        return "404"
    return send_from_directory(path, filename= filename, as_attachment=True)


@main.route('/')
def index():
    return render_template('index.html')