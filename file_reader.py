import json


def open_file(fileName):
    f = open('./data/'+fileName)
    data = json.load(f)
    f.close()
    return data


def get_users():
    users = open_file('users.json')
    return users


def add_user(username, password, type, pl):
    users = get_users()
    user = {
        "password": password,
        "type": type,
        "pl": pl
    }
    users[username] = user
    f = open('./data/users.json', 'w')
    json.dump(users, f)


def get_records():
    records = open_file('records.json')
    return records


def save_records(records):
    f = open('./data/records.json', 'w')
    json.dump(records, f)
