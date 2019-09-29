from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = "b'\xedl\x9eL\x9c;=\x9a\xb2\xeb\x89&\x9b6\xcd\x8b\xb3dF\xf4q\xfa\xc7S"
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print("Message delivered.")

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print("My event received: " + str(json))
    socketio.emit('my response', json, callback=messageReceived)



if __name__ == "__main__":
    socketio.run(app, debug = True)
