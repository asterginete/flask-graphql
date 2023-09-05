import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

def validate_password(password):
    # At least 8 characters, 1 uppercase, 1 lowercase, 1 number
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
    return re.match(pattern, password) is not None
