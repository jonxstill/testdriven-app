import os
import sys
from flask import Flask, jsonify

# Instantiate the app
app = Flask(__name__)

# Set Config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)


@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
