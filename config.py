from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False  # Don't sort json keys of jsonify on json response

# The database URI that should be used for the connection.
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'planets.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)