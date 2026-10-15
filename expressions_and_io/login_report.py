MAX_LOGIN_ATTEMPTS=5
username=input("username:")
failed_attempts=int(input("failed attempts:"))
attempts_left=MAX_LOGIN_ATTEMPTS-failed_attempts
print("="*30)
print("LOGIN REPORT")
print("="*30)
print(f"User:\t{username}")
print(f"Failed:\t{failed_attempts}")
print(f"Attempts left:\t{attempts_left}")
