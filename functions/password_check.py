def long_enough(password, minimum=8):
    return len(password) >= minimum


def differs_from_username(password, username):
    return password != username


def password_ok(password, username):
    enough = long_enough(password)
    different = differs_from_username(password, username)
    return enough and different


username = input("Username: ")
password = input("Password: ")

if password_ok(password, username):
    print("Password accepted.")
else:
    print("Password rejected.")