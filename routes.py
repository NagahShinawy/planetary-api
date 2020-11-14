from config import *
from random import choice


@app.route('/',  strict_slashes=False)
def index():
    return 'Hello World'


@app.route('/about',  strict_slashes=False)
def about():
    return 'ABOUT'


@app.route('/contact',  strict_slashes=False)
def contact():
    return 'contact'


@app.route('/courses',  strict_slashes=False)
def courses():
    return 'courses'


@app.route('/players',  strict_slashes=False)
def players():
    pls = """
    <ul>
        <li style='color:red;'>Mo Salah</li>
        <li style='color:blue;'>Messi</li>
        <li style='color:green;'>Ronaldo</li>
    </ul>
    """
    return pls


@app.route('/players/<player_name>',  strict_slashes=False)
def player(player_name):
    pname = player_name.lower()
    if pname == 'salah':
        return "<li style='color:red;'>Mo Salah</li>"
    if pname == 'ronaldo':
        return "<li style='color:green;'>Ronaldo</li>"
    if pname == 'messi':
        return "<li style='color:blue;'>Messi</li>"
    return f" '{player_name}' Player Not Found"


@app.route('/create-player',  strict_slashes=False, methods=['POST'])
def create_player():
    plys = ['Nymar', 'Zidane', 'maradona']
    pl = choice(plys)
    return {
        'player': pl
    }


@app.route('/captain',  strict_slashes=False, methods=['GET'])
def captain():
    coaches = {
        "liverpool": "Clob",
        "Tottnham": "Morinho",
        "man united": "sir alex",
        "real madrid": "zidane",
    }
    # coaches.update({"msg": "top coaches"})
    # return jsonify(msg="top football coaches", count=10)
    # return jsonify(coaches)
    return jsonify(**coaches)
