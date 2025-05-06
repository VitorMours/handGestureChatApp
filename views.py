from flask import Blueprint, render_template

bp = Blueprint("bp", __name__, template_folder="template")

@bp.route("/base", methods=["GET"])
def base():
  return render_template("base.html")

@bp.route("/", methods=["GET"])
def index():
  return render_template("index.html")