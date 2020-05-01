from interface import patient_prompt
from records import get_user_records


def patient_role(patient):
    login = True
    while(login):
        choice = patient_prompt()
        if choice == 0:
            get_user_records(patient['pl'], username=patient['username'])
        elif choice == 1:
            login = False
        elif choice == 2:
            exit()
