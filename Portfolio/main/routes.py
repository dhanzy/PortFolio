import os

from flask import render_template, Blueprint, send_file, send_from_directory



main = Blueprint('main', __name__)


@main.route('/manifest.webmanifest')
def webmanifest():
    path = r'static\manifest.webmanifest'
    return send_file(path, as_attachment=True)



@main.route('/resume.pdf')
def resume():
    # path = os.path.join('Portfolio','static')
    # if not os.path.exists(os.path.join(path, filename)):
    #     return os.getcwd()
    return send_file(r'static\resume.pdf', as_attachment=True)
    # return send_from_directory(path, filename=filename, as_attachment=True)


@main.route('/')
def index():
    return render_template('index.html')