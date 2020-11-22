from planetary_api.config import *
from random import choice
from planetary_api.models import db, User, Planet, \
    user_schema, users_schema, planet_schema, planets_schema
from werkzeug.security import generate_password_hash, check_password_hash

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
    results = planets_schema.dumps(plts)  # return string looks like list of dics but string
    results = planets_schema.dump(plts)   # return list of dics
    # return jsonify(results)
    return jsonify(results)


@app.route("/planets/<int:planet_id>", strict_slashes=False, methods=['GET'])
def single_planet(planet_id: int):
    plt = Planet.query.filter_by(planet_id=planet_id).first()
    if plt:
        return jsonify(data=planet_schema.dump(plt))
    return jsonify(msg='This Planet does not exist')


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
    usrs = users_schema.dump(User.query.all())
    return jsonify(usrs)


@app.route("/users/<string:user_id>", strict_slashes=False, methods=['GET'])
def single_user(user_id: int):
    usr = User.query.filter_by(user_id=user_id).first()
    if usr:
        return jsonify(data=user_schema.dump(usr))
    return jsonify(msg='This user does not exist'), 404


@app.route("/register", methods=['POST'])
def register():
    # email = request.form['email']
    # email = request.json['email']  # if request comes from json body
    email = request.form['email']  # if request comes from form data
    is_user_found = User.query.filter(User.email.ilike(email))
    # is_found = User.query.filter_by(email=email).first()
    if is_user_found.count() > 0:
        return jsonify(msg=f'email ({is_user_found.first().email}) already found'), 409  # mean conflict
    password = request.form.get('password')
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    if not all([fname, lname, password]):
        return jsonify(msg='Missing required info'), 400   # means bad request
    user = User(fname=fname, lname=lname, password=generate_password_hash(password), email=email)
    session.add(user)
    session.commit()
    pwdhash = user.password
    print(check_password_hash(pwdhash, password))
    return jsonify(msg=f'user ({fname}) was added successfully'), 201  # mean created


@app.route('/login', methods=['POST'])
def login():
    if request.is_json:   # check if data comes from json or html form
        data = request.json
    else:
        data = request.form
    email = data.get('email')
    password = data.get('password')
    # user = User.query.filter_by(email=email, password=password).first()
    user = User.query.filter_by(email=email).first()
    if user:
        hashed_password = user.password
        if check_password_hash(hashed_password, password):
            token = create_access_token(identity=email)
            return jsonify(token=token), 200
    return jsonify(msg="incorrect email or password"), 401  # mean permissions denied


@app.route('/reset-password/<string:email>', methods=['GET'])
def reset_password(email: str):
    user = User.query.filter_by(email=email).first()
    if user:
        msg = Message(subject='Reset Password',
                      sender='admin@api.com', recipients=[user.email], body='Your password is "' + user.password + '"')
        mail.send(msg)
        return jsonify(msg='Password sent to ' + user.email), 200

    return jsonify(msg='Invalid email'), 401  # means unauthorized.


@app.route('/add-planet', methods=['POST'])
@jwt_required   # securing endpoint
def add_planet():
    if request.is_json:
        data = request.json
    else:
        data = request.form
    planet_name = data.get('planet_name')
    planet_type = data.get('planet_type')
    home_star = data.get('home_star')
    mass = data.get('mass')
    radius = data.get('radius')
    distance = data.get('distance')
    params = [planet_name, planet_type, home_star, mass, radius, distance]
    plt = Planet.query.filter_by(planet_name=planet_name).first()
    if plt:
        return jsonify(msg='Planet "{}" is already exist'.format(planet_name)), 409  # mean conflict
    if not all(params):
        return jsonify(msg='Missing data'), 400
    plt = Planet(planet_name=planet_name,
                 planet_type=planet_type, home_star=home_star, mass=mass, radius=radius, distance=distance)
    session.add(plt)
    session.commit()
    return jsonify(data=planet_schema.dump(plt)), 201  # means new row created


@app.route('/update-planet/<int:planet_id>', methods=['PUT'])
@jwt_required   # securing endpoint
def update_planet(planet_id):
    if request.is_json:
        data = request.json
    else:
        data = request.form
    planet = Planet.query.filter_by(planet_id=planet_id).first()
    if not planet:
        return jsonify(msg=f"Planet with id '{planet_id}' is not exist"), 404
    planet_name = data.get('planet_name')
    if planet_name is not None:
        planet.planet_name = planet_name
    planet_type = data.get('planet_type')
    if planet_type is not None:
        planet.planet_type = planet_type
    home_star = data.get('home_star')
    if home_star is not None:
        planet.home_star = home_star

    mass = data.get('mass')
    if mass is not None:
        planet.mass = mass

    radius = data.get('radius')
    if radius is not None:
        planet.radius = radius

    distance = data.get('distance')
    if distance is not None:
        planet.distance = distance

    session.commit()
    params = [planet_name, planet_type, home_star, mass, radius, distance]
    if any(params):
        # return jsonify(msg=f"Planet '{planet.planet_name}' is updated successfully")
        return jsonify(data=planet_schema.dump(planet))
    return jsonify(msg='No params passed to update'), 400