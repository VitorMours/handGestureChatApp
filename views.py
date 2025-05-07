from flask import Blueprint, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO, emit, send, leave_room, join_room

bp = Blueprint("bp", __name__, template_folder="template")
rooms = {}
socketio = SocketIO()

@bp.route("/base", methods=["GET"])
def base():
  return render_template("base.html")

@bp.route("/room/<room_code>")
def room(room_code):
    room_code = session["room_code"]
    name= session["name"]

    if room_code not in rooms or name is None or room_code is None:
      return render_template(url_for("index"))
    
    return render_template("room.html")

@bp.route("/", methods=["GET","POST"])
def index():
  session.clear()
  if request.method == "GET":
    return render_template("index.html")
  if request.method == "POST":
    name = request.form.get("name")
    room_code = request.form.get("room_code")
    session["room_code"] = room_code
    session["name"] = name
    print(f"The user: {name} enter the room: {room_code}")
    return redirect(url_for("bp.room", room_code = room_code))
  


@socketio.on("connect")
def conection_handler(auth):
  name = session["name"]
  room_code = session["room_code"]

  if not room or not name:
    return 
  if room not in rooms:
    leave_room(room)
    return 
  join_room(room)
  send({"name" : name, "message": "has entered the room"}, to=room_code)
  rooms[room]["members"] += 1
