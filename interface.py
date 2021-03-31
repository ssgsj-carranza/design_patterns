from checkemail import check


def interface():
    while True:
        first_name = input("Please enter first name: ")
        last_name = input("Please enter last name: ")
        email_address = input("Please enter email address: ")
        check(email_address)
        if first_name.isalpha():
            break
        else:
            print("Please enter name A-Z characters")
        if last_name.isalpha():
            break
        else:
            print("Please enter last name A-z characters")
