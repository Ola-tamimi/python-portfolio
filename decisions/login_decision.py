# Check login information.
# Decide if access is allowed.
MAX_FAILED=5
KNOWN_USER="analyst"
STORED_PASSWORD="Blue#Falcon72"
username=input("Enter your username:")
failed=int(input("Enter failed attempts so far:"))
password=input("password:")
if failed>=MAX_FAILED:
    print("Account locked.")
elif username!= KNOWN_USER:
    print("Unknown user.")  
elif password != STORED_PASSWORD:
    print(f"Access denied. Attempts left: {MAX_FAILED - failed - 1}")
else:
    print("Access granted.")
 