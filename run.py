# from app import app
# app.run(debug=True)

from app import socketio, app
socketio.run(app)


@socketio.on('message')
def handle_message(msg):
    print("Received the following message: " + msg)
    send(msg, broadcast=True)
