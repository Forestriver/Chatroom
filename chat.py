from gevent import monkey
monkey.patch_all()
import os
from os import environ
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
from flask import session

load_dotenv(find_dotenv())
app = Flask(__name__)
#Creating path to the file with secret key
app.config['SECRET_KEY'] = environ.get('KEY')
socketio = SocketIO(app, async_mode='gevent', engineio_logger=True, cors_allowed_origins='*', manage_session = False)


@app.route('/')
def index():
    return render_template('session.html')


@socketio.on('message')
def handle_message(msg):
    send(msg, broadcast = True)

@socketio.on('join')
def join_username(username):
    emit('message', {'user':'Chat', 'message':username  + ' joined this chatroom'}, broadcast = True)
    socketio.sleep(0)


if __name__ == '__main__':
    socketio.run(app, debug=True)
