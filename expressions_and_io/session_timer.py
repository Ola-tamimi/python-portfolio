session_length_in_seconds=int(input("Enter the session length in seconds"))
minutes=session_length_in_seconds//60
secondes=session_length_in_seconds%60
print(f"session length is secconds:{session_length_in_seconds}\nsession length:{minutes} minutes\nand{secondes} secons")
# 905 -> 15 minutes and 5 seconds
# 60 -> 1 minute and 0 seconds
# 59 -> 0 minutes and 59 seconds