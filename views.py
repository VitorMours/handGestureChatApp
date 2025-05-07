from flask import Blueprint, render_template, request, session, redirect, url_for

bp = Blueprint("bp", __name__, template_folder="template")

@bp.route("/base", methods=["GET"])
def base():
  return render_template("base.html")

@bp.route("/room/<room_code>/", methods=["GET", "POST"])
def room(room_code):
  if request.method == "GET":
    return render_template("room.html")
  elif request.method == "POST":
    return render_template("room.html", room_code=room_code)



@bp.route("/", methods=["GET","POST"])
def index():
  if request.method == "GET":
    return render_template("index.html")
  if request.method == "POST":
    session["name"] = request.form.get("name")
    room_code = request.form.get("room_code")
    return redirect(url_for("bp.room", room_code=room_code))