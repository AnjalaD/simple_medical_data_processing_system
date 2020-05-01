from interface import staff_prompt
from records import get_user_records, add_user_record


def staff_role(staff):
    login = True
    while(login):
        choice = staff_prompt()
        if choice == 0:
            get_user_records(staff['pl'])
        elif choice == 1:
            add_user_record(staff['pl'])
        elif choice == 2:
            login = False
        elif choice == 3:
            exit()
