from flask import Flask, jsonify
import json

app = Flask(__name__)

CONFIG_FILE = "config.json"

@app.route('/panel-version', methods=['GET'])
def get_panel_version():
    with open(CONFIG_FILE, 'r') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
