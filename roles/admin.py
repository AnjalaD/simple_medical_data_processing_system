from interface import admin_prompt
from auth import register


def admin_role(admin):
    login = True
    while(login):
        choice = admin_prompt()
        if choice == 0:
            register()
        elif choice == 1:
            login = False
        elif choice == 2:
            exit()
