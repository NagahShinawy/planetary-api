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
