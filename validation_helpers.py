import re

def valid_username(username):
    username_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    checkname = username_RE.match(username)
    if checkname is None:
        return False
    return True

def valid_password(password):
    password_RE = re.compile(r"^.{3,20}$")
    checkpwd = password_RE.match(password)
    if checkpwd is None:
        return False
    return True

def valid_email(email):
    email_RE = re.compile(r"^[\S]+@[\S]+[.][\S]+$")
    checkemail = email_RE.match(email)
    if checkemail is None:
        return False
    return True
