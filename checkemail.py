import re

regex = "^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$"


def check(email_address):
    if re.search(regex, email_address):
        print("Valid email")
    else:
        print("Invalid email, please enter valid email")
