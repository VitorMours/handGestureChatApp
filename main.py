from flask import Flask, render_template # type: ignore
from views import bp
from sockets import socketio


def create_app() -> Flask:
  app = Flask(__name__)
  app.config["SECRET_KEY"] = "secret_key_for_server_in_websockets"

  app.register_blueprint(bp)
  socketio.init_app(app)
  return app

if __name__ == "__main__":
  app = create_app()
  socketio.run(app, debug=True)
