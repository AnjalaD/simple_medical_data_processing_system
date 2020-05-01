from file_reader import get_users, add_user
from interface import login_prompt, register_prompt
import hashlib


def login():
    data = login_prompt()
    username = data['username']
    password = data['password']

    users = get_users()
    if username in users:
        password = hashlib.md5(password.encode()).hexdigest()

        if password == users[username]['password']:
            print('\n\n----Welcome!'
                  + username
                  + '----\n You are logged in as '+users[username]['type'])
            user = users[username]
            user['username'] = username
            return user

    print('!!----Invalid credentials----!!\n')
    return False


def register():
    data = register_prompt()
    username = data['username']
    password = data['password']
    type = data['type']
    pl = data['pl']

    if username not in get_users():
        password = hashlib.md5(password.encode()).hexdigest()
        add_user(username, password, type, pl)
        print('----Success!---- \nNew user: '+username+'\n')
        return True
    print('Username already exsits! \n')
    return False
