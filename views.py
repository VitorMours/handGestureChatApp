from flask import Blueprint, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO, emit, send, leave_room, join_room

bp = Blueprint("bp", __name__, template_folder="template")
rooms = {}
socketio = SocketIO()

@bp.route("/base", methods=["GET"])
def base():
  return render_template("base.html")

@bp.route("/", methods=["GET","POST"])
def index():
  session.clear()
  if request.method == "GET":
    return render_template("index.html")
  if request.method == "POST":
    name = request.form.get("name")
    session["room_code"] = request.form.get("room_code")
    session["name"] = name
    room_code = session["room_code"]    
    print(f"The user: {name} enter the room: {room_code}")
    return redirect(url_for("bp.room"))
  
@bp.route("/room")
def room():
    room_code = session["room_code"]
    name = session["name"]
    return render_template("room.html", room_code=room_code)

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


@socketio.on("message")
def message_handler(data):
  room_code = session.get("room_code")
  print(data)
  content = {
    "name":session.get("name"),
    "message":data["data"]
  } 
  print(content)
  send(content, to=room_code)
  rooms[room_code]["messages"].append(content)
