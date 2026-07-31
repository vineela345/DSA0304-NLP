import re

def validate_email(email):
    pattern = r'^[A-Za-z][A-Za-z0-9._]*@[A-Za-z]+\.(com|org|edu|net|in)$'
    return re.match(pattern, email) is not None

def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&!]).{8,}$'
    return re.match(pattern, password) is not None

def validate_mobile(mobile):
    pattern = r'^[6-9]\d{9}$'
    return re.match(pattern, mobile) is not None

email = input("Enter Email: ")
password = input("Enter Password: ")
mobile = input("Enter Mobile Number: ")

if validate_email(email):
    print("Valid Email")
else:
    print("Invalid Email")

if validate_password(password):
    print("Strong Password")
else:
    print("Weak Password")

if validate_mobile(mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")
