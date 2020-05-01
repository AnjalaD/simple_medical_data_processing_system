from interface import main_prompt
from auth import login
from roles.admin import admin_role
from roles.staff import staff_role
from roles.patient import patient_role

while True:
    choices = main_prompt()

    if choices == 0:
        user = login()
        if(user != False):
            if(user['type'] == 'Admin'):
                admin_role(user)
            elif(user['type'] == 'Staff'):
                staff_role(user)
            elif(user['type'] == 'Patient'):
                patient_role(user)
    elif choices == 1:
        exit()
