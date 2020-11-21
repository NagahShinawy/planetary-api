from flask import Flask, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_mail import Mail, Message

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False  # Don't sort json keys of jsonify on json response

# The database URI that should be used for the connection.
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'planets.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


app.config['JWT_SECRET_KEY'] = 'super-secret'   # CHANGE IT


# mail conf from ==> mailtrap.io  ==> flask-mail
app.config['MAIL_SERVER'] = "smtp.mailtrap.io"
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
# app.config['MAIL_USERNAME'] = '382aac1d0d143e'
# app.config['MAIL_PASSWORD'] = 'e3e6141063063b'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
mail = Mail(app)
