from flask import (
  Flask,
)
from markupsafe import escape

flask_app = Flask(__name__)
@flask_app.route("/<name>")
def flask_main(name):
    return f"Hello, {escape(name)} from Flask!"