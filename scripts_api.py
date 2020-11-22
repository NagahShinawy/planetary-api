import requests
import json


def search_player(name=None, age=None, team=None):
    search_endpoint = f'http://127.0.0.1:8000/search/?'
    if name:
        search_endpoint = f'http://127.0.0.1:8000/search/?name={name}'
    if age:
        search_endpoint = f'http://127.0.0.1:8000/search/?name={name}&age={age}'
    if team:
        search_endpoint = f'http://127.0.0.1:8000/search/?name={name}&age={age}&team={team}'

    response = requests.get(search_endpoint)
    print(response.status_code)
    if response.status_code == 200:
        players = response.json()
        with open('players.json', 'w') as f:
            json.dump(players, f, indent=4, sort_keys=False)
    return response.json()


def search_player_2(**kwargs):
    name = kwargs.get('name')
    age = kwargs.get('age')
    team = kwargs.get('team')
    search_endpoint = f'http://127.0.0.1:8000/search/?'
    params = {
        'name': name,
        'age': age,
        'team': team
    }
    res = requests.get(search_endpoint, params=params)
    print(res.status_code)
    print(res.reason)
    print(res.content)


def planets():
    plt_endpoints = "http://127.0.0.1:8000/planets"
    response = requests.get(plt_endpoints)
    print(response.status_code, 'Python Flask')
    print(response.json())


def users():
    users_endpoints = "http://127.0.0.1:8000/users"
    response = requests.get(users_endpoints)
    print(response.status_code, 'Users')
    print(response.json())


def login(email, password):
    login_endpoint = "http://127.0.0.1:8000/login"
    payload = {
        'email': email,
        'password': password
    }
    res = requests.post(login_endpoint, json=payload)
    if res.status_code == 200:
        return res.json()['token']
    return ''


def add_planet(email, password, **kwargs):
    token = login(email, password)
    data = {}
    plt_name = kwargs.get('planet_name')
    plt_type = kwargs.get('plt_type')
    home_star = kwargs.get('home_star')
    mass = kwargs.get('mass')
    radius = kwargs.get('radius')
    distance = kwargs.get('distance')
    if plt_name:
        data['planet_name'] = plt_name
    if plt_name:
        data['planet_type'] = plt_type
    if plt_name:
        data['home_star'] = home_star
    if mass:
        data['mass'] = mass
    if radius:
        data['radius'] = radius
    if distance:
        data['distance'] = distance
    data = {
        "planet_name": plt_name,
        "planet_type": plt_type,
        "home_star": home_star,
        "mass": mass,
        "radius": radius,
        "distance": distance
    }
    headers = {'Authorization': 'Bearer ' + token}  # is the equal of adding "Bearer token"  to add new row from postman
    res = requests.post("http://127.0.0.1:8000/add-planet", json=data, headers=headers)
    print(res.reason)


def update_planet(email, password, planet_id, **kwargs):
    token = login(email, password)
    data = {}
    plt_name = kwargs.get('planet_name')
    plt_type = kwargs.get('plt_type')
    home_star = kwargs.get('home_star')
    mass = kwargs.get('mass')
    radius = kwargs.get('radius')
    distance = kwargs.get('distance')
    if plt_name:
        data['planet_name'] = plt_name
    if plt_name:
        data['planet_type'] = plt_type
    if plt_name:
        data['home_star'] = home_star
    if mass:
        data['mass'] = mass
    if radius:
        data['radius'] = radius
    if distance:
        data['distance'] = distance
    data = {
        "planet_id": planet_id,
        "planet_name": plt_name,
        "planet_type": plt_type,
        "home_star": home_star,
        "mass": mass,
        "radius": radius,
        "distance": distance
    }
    headers = {'Authorization': 'Bearer ' + token}  # is the equal of adding "Bearer token"  to add new row from postman
    res = requests.put(f"http://127.0.0.1:8000/update-planet", json=data, headers=headers)
    print(res.reason)


def delete_planet(email, password, planet_id):
    token = login(email, password)
    payload = {
        'planet_id': planet_id
    }
    headers = {'Authorization': 'Bearer ' + token}
    res = requests.delete("http://127.0.0.1:8000/delete-planet", json=payload, headers=headers)
    print(res.reason)
