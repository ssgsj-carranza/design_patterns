from checkemail import check
import random
import string

random = "".join([random.choice(string.ascii_letters+string.digits) for n in range(10)])


def interface():
    while True:
        first_name = input("Please enter first name: ")
        last_name = input("Please enter last name: ")
        email_address = input("Please enter email address: ")
        check(email_address)
        print(f"This is your registration number:{random}")
        if first_name.isalpha():
            break
        else:
            print("Please enter name A-Z characters")
        if last_name.isalpha():
            break
        else:
            print("Please enter last name A-z characters")
