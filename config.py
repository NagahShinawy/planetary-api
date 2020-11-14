from flask import Flask, jsonify

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False  # Don't sort json keys of jsonify
