from flask import Flask, jsonify, request

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False  # Don't sort json keys of jsonify on json response
