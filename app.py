from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
# Allow requests from your Netlify URL (replace with your actual Netlify URL)
CORS(app, resources={r"/led": {"origins": "https://led-control.netlify.app/"}})

# In-memory LED state
led_state = {"led": "off"}

@app.route('/led', methods=['GET'])
def get_led_state():
    return jsonify(led_state)

@app.route('/led', methods=['POST'])
def set_led_state():
    global led_state
    data = request.get_json()
    if 'led' in data and data['led'] in ['on', 'off']:
        led_state = {"led": data['led']}
        return jsonify({"message": "LED state updated", "led": led_state['led']}), 200
    return jsonify({"error": "Invalid LED state"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
