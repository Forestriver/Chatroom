from os import environ
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
from flask import session

load_dotenv(find_dotenv())
app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get('KEY')
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('session.html')

@socketio.on('message')
def handle_message(msg):
    print(msg)
    send(msg, broadcast = True)

@socketio.on('join')
def join_username(username):
    emit('message', {'user':'Server', 'message':username  + ' joined the chat'}, broadcast = True)


if __name__ == '__main__':
    socketio.run(app, debug=True)
