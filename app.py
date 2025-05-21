from flask import Flask, render_template 
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='eventlet')

online_users = set()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/music')
def music():
    return render_template('music.html')

@app.route('/draw')
def draw():
    return render_template('draw.html')

@app.route('/hug')
def games():
    return render_template('hug.html')

@socketio.on('play')
def handle_play():
    emit('play', broadcast=True)

@socketio.on('pause')
def handle_pause():
    emit('pause', broadcast=True)

@socketio.on('sync')
def handle_sync(data):
    emit('sync', data, broadcast=True)
    
@socketio.on('change_song')
def handle_change_song(song_path):
    emit('change_song', song_path, broadcast=True)

@socketio.on('sync_time')
def handle_sync_time(time):
    emit('sync_time', time, broadcast=True)

@socketio.on('draw_data')
def handle_draw(data):
    emit('draw_data', data, broadcast=True)
@socketio.on('clear_canvas')
def handle_clear():
    emit('clear_canvas', broadcast=True, include_self=False)

@socketio.on('chat_message')
def handle_chat_message(msg):
    emit('chat_message', msg, broadcast=True)
    
@socketio.on('send_hug')
def handle_hug():
    emit('receive_hug', broadcast=True)
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port)
