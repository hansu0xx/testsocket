# --- Flask and Flask-SocketIO Imports ---
import threading
import time
from flask import Flask, render_template
from flask_socketio import SocketIO, emit


global_simulator_data = {}


# --- Flask App Setup ---
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here' # IMPORTANT: Change this for production!
socketio = SocketIO(app, cors_allowed_origins="*") # Allow all origins for development


@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    global global_simulator_data
    print('Client connected')
    # When a client connects, send the current snapshot immediately if available
    
    emit('trading_data_update', global_simulator_data)

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


def start_simulator():
    global global_simulator_data
    time.sleep(1)
    while True:
        unix_time = int(time.time())
        global_simulator_data = {
            "time": unix_time
        }
        time.sleep(0.5)
     

def update_data():
    global global_simulator_data
    time.sleep(1)
    while True:
        # simulator_data += f" {time.strftime('%H:%M:%S')}"
        socketio.emit('trading_data_update', global_simulator_data)
        time.sleep(1)


if __name__ == '__main__':
    simulator_thread = threading.Thread(target=start_simulator, daemon=True)
    simulator_thread.start()

    update_thread = threading.Thread(target=update_data, daemon=True)
    update_thread.start()
    
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True, host="0.0.0.0", port=5000, use_reloader=False)

    print("Application stopped.")
