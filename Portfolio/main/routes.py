import os
import json

from flask import (
    make_response,
    render_template,
    Blueprint,
    send_file,
    send_from_directory,
)

main = Blueprint("main", __name__)


@main.route("/<filename>")
def get_static_files(filename):
    path = os.path.join("static", filename)
    return send_file(path, as_attachment=True)
    # return send_from_directory(path, filename=filename, as_attachment=True)


@main.route("/service-worker.js")
def serviceWorker():
    response = make_response(
        send_from_directory("static", path="/", filename="ServiceWorker.js")
    )
    response.headers["Content-Type"] = "application/javascript"
    return response


@main.route("/")
def index():
    with open("Portfolio/config.json", "r") as f:
        data = json.loads(f.read())
    return render_template("index.html", data=data)
