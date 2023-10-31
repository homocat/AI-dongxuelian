from flask import (
  Flask,
  request
)
from markupsafe import escape

flask_app = Flask(__name__)
@flask_app.route("/")
def flask_main():
    name = request.args.get("name", "World")
    return f"Hello, {escape(name)} from Flask!"