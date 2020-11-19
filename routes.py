from planetary_api.config import *
from random import choice
from planetary_api.models import db, User, Planet, \
    user_schema, users_schema, planet_schema, planets_schema

session = db.session


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
    return jsonify(**coaches), 200


@app.route('/not_found')
def not_found():
    return jsonify(messgage='not found'), 404


@app.route('/search', strict_slashes=False, methods=['GET'])
def search():
    name = request.args.get('name')
    try:
        age = int(request.args.get('age'))
    except Exception:
        age = None
    team = request.args.get('team')
    if age is not None and age < 18:
        return jsonify({'msg': 'unauthorized user under 18 years old'}), 401  # unauthorized status code
    info = [name, age, team]
    if all(info):
        return jsonify(name=name, age=age, team=team)
    return jsonify({'msg': 'missing some player info'}), 400   # 400 missing data


@app.route('/player-info/<string:player_name>/<int:player_number>')
def player_info(player_name: str, player_number: int):
    if player_number in [7, 10, 11, 14, 22, 17]:
        msg = 'best players number {}'.format(player_number)
    else:
        msg = 'normal number'
    return jsonify(name=player_name, number=player_number, message=msg)


@app.route("/planets", strict_slashes=False, methods=['GET'])
def planets():
    plts = Planet.query.all()
    print(plts)
    plts = [{'pname': p.planet_name, "type": p.planet_type, "home-star": p.home_star, "mass": p.mass} for p in plts]
    print("Testing request")
    # return jsonify(plts)
    return jsonify(data=plts)


# using Marshmallow
@app.route("/planets-list", strict_slashes=False, methods=['GET'])
def planets_list():
    plts = Planet.query.all()
    results = planets_schema.dumps(plts)  # return string looks like list of dics
    results = planets_schema.dump(plts)   # return list of dics
    # return jsonify(results)
    return jsonify(results)


@app.route("/users", strict_slashes=False, methods=['GET'])
def users():
    usrs = User.query.all()
    print(usrs)
    usrs = [{"ID": user.user_id, "first name": user.fname, "last name": user.lname, "email": user.email} for user in usrs]
    # nagah = User.query.filter_by(fname='nagah')
    nagah = User.query.filter(User.fname.ilike("naGah"))  #
    if nagah.count() > 0:
        nagah = nagah.first()
    else:
        return jsonify({})
    print("Testing request Users")
    # return jsonify(usrs)

    return jsonify(fisrtname=nagah.fname, lastname=nagah.lname, email=nagah.email)


# using Marshmallow
@app.route("/users-list", strict_slashes=False, methods=['GET'])
def users_list():
    pass