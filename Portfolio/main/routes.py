from flask import render_template, Blueprint, send_file


main = Blueprint('main', __name__)


@main.route('/manifest.webmanifest')
def webmanifest():
    path = r'static\manifest.webmanifest'
    return send_file(path, as_attachment=True)

@main.route('/')
def index():
    return render_template('index.html')