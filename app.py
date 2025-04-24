from flask import Flask, jsonify, request
import json

app = Flask(__name__)
LED_STATE_FILE = 'led_state.json'

@app.route('/led/<state>', methods=['POST'])
def set_led(state):
    if state not in ['on', 'off']:
        return jsonify({'error': 'Invalid state'}), 400
    with open(LED_STATE_FILE, 'w') as f:
        json.dump({'led': state}, f)
    return jsonify({'status': 'ok', 'led': state})

@app.route('/led/status', methods=['GET'])
def get_led_status():
    try:
        with open(LED_STATE_FILE, 'r') as f:
            state = json.load(f)
        return jsonify(state)
    except:
        return jsonify({'led': 'off'})  # default
