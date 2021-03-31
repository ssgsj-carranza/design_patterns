import random

applicants = [{
    "first_name": "Sam",
    "last_name": "Samson",
    "email_address": "samsamson@gmail.com",
    "registration_number": 123456
    },
    {"first_name": "Peter",
     "last_name": "Peterson",
     "email_address": "peterpeterson@gmail.com",
     "registration_number": 456789
     },
    {"first_name": "Tim",
     "last_name": "Timson",
     "email_address": "timtimsonson@gmail.com",
     "registration_number": 124578
     }]

key_list = list(applicants.keys())
val_list = list(applicants.values())

def pick_winner():
    random_entry = random.choice(list(val_list))
    print(f' The winner is {random_entry}')