# fix_the_policy.py
# Check a new password against an example policy and classify its length.
MIN_LENGTH = 12

username = input("Username: ")
password = input("New password: ")
# syntax error:(Add the missing colon)
if len(password) < MIN_LENGTH:
    print("- Too short.")
 # semantic error:(check both conditions independently)
if password == username:
    print("- Same as the username.")

if len(password) >= MIN_LENGTH:
    strength = "acceptable"
# semantic error:(check long passwords first)
if len(password) >= 16:
    strength = "long"
elif len(password) >= MIN_LENGTH:
    strength="acceptable"  
else:
    strength = "short"
# semantic error:(print for every password)
print(f"Length: {len(password)} ({strength})")