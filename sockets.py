from flask_socketio import SocketIO 

socketio = SocketIO()

@socketio.on("connect")
def connection_created():
    pass

@socketio.on("disconnect")
def connection_killed():
    pass 

@socketio.on("message")
def message(message):
    pass




