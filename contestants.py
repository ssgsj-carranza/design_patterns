from checkemail import check
import random
import string

registration_number = "".join([random.choice(string.ascii_letters + string.digits) for n in range(10)])


class Contestant:
    def __init__(self):
        self.first_name = input("Please enter first name: ")
        self.last_name = input("Please enter last name: ")
        self.email_address = input("Please enter email address: ")
        check(self.email_address)
        self.registration_number = registration_number
        print(f"This is your registration number:{registration_number}")
        if not self.first_name.isalpha() or not self.last_name.isalpha():
            print("Please enter characters A-Z")

    def notify(self, is_winner):
        if is_winner is True:
            print(f"Congratulations {self.first_name} {self.last_name} you are the winner!!!")
        else:
            print("We have chosen a winner, thanks for participating")
