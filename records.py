from interface import username_prompt, user_records_prompt, create_patient_record_prompt,  create_session_record_prompt, patient_details_prompt
from file_reader import get_records, save_records


def prepare_for_prompt(records):
    choices = []
    for i in records:
        choices.append(i['date'])
    choices.append("Back")
    return choices


def view_records(pl, session_records):
    back = False
    while(not back):
        choice = user_records_prompt(prepare_for_prompt(session_records))
        if(choice != len(session_records)):
            record = session_records[choice]

            if pl <= record['pl']:
                print("\t\tDate: " + record['date'])
                print("\t\tSickness Details: " + record['sickness_details'])
                print("\t\tDrugs: ")
                for i in record['drugs'].split(','):
                    print('\t\t\t'+i)
                print("\t\tTests: ")
                for i in record['tests'].split(','):
                    print('\t\t\t'+i)
            else:
                print('\t!!!---You do not have access---!!!\n')

            print()
        else:
            back = True


def get_user_records(pl, username=None):
    owner = True
    if username == None:
        owner = False
        username = username_prompt()

    records = get_records()
    if username in records:

        user_record = records[username]
        print("\n ----Patient record found!----\n")
        if(pl <= user_record['pl'] or owner):
            print('\tName: ' + user_record['name'])
            print('\tAge: ' + user_record['age'])
            print('\tTelephone: ' + user_record['telephone'])
            print()
            session_records = user_record['records']
            view_records(pl, session_records)
        else:
            print('!!!----You do not have access----!!!\n')

    else:
        print('----No patient record found!----\n')


def add_user_record(pl):
    username = username_prompt()
    records = get_records()
    if username not in records:
        choice = create_patient_record_prompt()
        if(choice == 0):
            patient = patient_details_prompt()
            records[username] = patient
            records[username] = pl
            records[username]['records'] = []
        elif(choice == 1):
            return

    user_record = records[username]
    print("\n Patient record found! (for "
          + username
          + ")\nEnter session details below : ")
    if pl <= user_record['pl']:
        print('\tName :' + user_record['name'])
        print('\tAge :' + user_record['age'])
        print('\tTelephone :' + user_record['telephone'])

        record = create_session_record_prompt()
        user_record['records'].append(record)
        save_records(records)
    else:
        print('!!!----You do not have access----!!!\n')
