from os import environ
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

load_dotenv(find_dotenv())
app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get('KEY')
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print("Message delivered.")

@socketio.on('connection')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print("My event received: " + str(json))
    socketio.emit('message', json, callback=messageReceived)



if __name__ == "__main__":
    socketio.run(app, debug = True)
