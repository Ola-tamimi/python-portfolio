
# fix_the_session.py
# This program reports a user's session time.

username = input("Username: ")
#Runtime error, fix:convert input to int
total_seconds = int(input("Session length in seconds: "))
#semantic error, fix:use floor division for whole minutes
minutes = total_seconds // 60
seconds = total_seconds % 60
print("=" * 30)
#semantic error,fix:use f-string to display the username
print(f"User: {username}")
#Runtime error, fix:convert minutes to str
print("Session: " + str(minutes )+ " min " + str(seconds) + " s")
print("=" * 30)
