from PyInquirer import prompt


def choices_prompt(choices, label):
    questions = [
        {
            'type': 'list',
            'name': 'choice',
            'message': label,
            'choices': choices,
            'filter': lambda x: choices.index(x)
        },
    ]
    answers = prompt(questions)
    return answers['choice']


def main_prompt():
    choices = ['Login', 'Exit']
    return choices_prompt(choices, 'Welcome to Medical Data Processing system!')

# ------------------auth-


def login_prompt():
    questions = [
        {
            'type': 'input',
            'name': 'username',
            'message': 'Enter username :',
        },
        {
            'type': 'password',
            'name': 'password',
            'message': 'Enter password :',
        }
    ]
    answers = prompt(questions)
    return answers


def register_prompt():
    pl = ['Specilist Doctors only', 'Doctors & above',
          'Nurses & above', 'Patient & above']
    questions = [
        {
            'type': 'input',
            'name': 'username',
            'message': 'Enter username :',
        },
        {
            'type': 'list',
            'name': 'type',
            'message': 'Select account type :',
            'choices': ['Patient', 'Staff', 'Admin'],
        },
        {
            'type': 'list',
            'name': 'pl',
            'message': 'Select privilage level:',
            'choices': pl,
            'filter': lambda x: pl.index(x)
        },
        {
            'type': 'password',
            'name': 'password',
            'message': 'Create password :'
        }
    ]
    answers = prompt(questions)
    return answers


# ------------------roles-


def admin_prompt():
    choices = ['Register new user', 'Logout', 'Exit']
    return choices_prompt(choices, 'Next :')


def staff_prompt():
    choices = ['View patient records', 'Add patient record', 'Logout', 'Exit']
    return choices_prompt(choices, 'Next :')


def patient_prompt():
    choices = ['View my records', 'Logout', 'Exit']
    return choices_prompt(choices, 'Next :')


# ------------------records-


def username_prompt():
    questions = [
        {
            'type': 'input',
            'name': 'username',
            'message': 'Enter username :',
        },
    ]
    answers = prompt(questions)
    return answers['username']


def user_records_prompt(choices):
    return choices_prompt(choices, 'Select Record :')


def create_patient_record_prompt():
    choices = ['Create new patient record', 'Back']
    return choices_prompt(choices, 'Patient record dose not exsist : ')


def patient_details_prompt():
    questions = [
        {
            'type': 'input',
            'name': 'name',
            'message': 'Patient name : ',
        },
        {
            'type': 'input',
            'name': 'age',
            'message': 'Patient age : ',
        },
        {
            'type': 'input',
            'name': 'telephone',
            'message': 'Patients telephone : ',
        },
    ]
    answers = prompt(questions)
    return answers


def create_session_record_prompt():
    pl = ['Specilist Doctors only', 'Doctors & above',
          'Nurses & above', 'Patient & above']
    questions = [
        {
            'type': 'input',
            'name': 'date',
            'message': 'Date : ',
        },
        {
            'type': 'input',
            'name': 'sickness_details',
            'message': 'Sickness details:',
        },
        {
            'type': 'input',
            'name': 'drugs',
            'message': 'Drug prescriptions : (as a comma separated list)',
        },
        {
            'type': 'input',
            'name': 'tests',
            'message': 'Lab test prescriptions : (as a comma separated list)',
        },
        {
            'type': 'list',
            'name': 'pl',
            'message': 'Set privilage level to record: ',
            'choices': pl,
            'filter': lambda x: pl.index(x)
        }
    ]
    answers = prompt(questions)
    return answers
