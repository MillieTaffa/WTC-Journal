from validator_collection import validators, checkers, errors

email_address = input("Enter email address: ")

try:
    if checkers.is_email(email_address):
        print("Valid")
except errors.InvalidEmailError:
    print("Invalid")
