# fix_the_rules.py
 # This program checks a connection against three rules.

role = input("Role: ")
#Runtime error  fix:convert port input to integer
port =int (input("Port: "))
#semantic error  fix:use == for comparison
is_admin = role == "admin"
# syntax error fix:<=
is_system_port = port <= 1023
# Semantic error fix: compare port with both values
is_web_port = port == 80 or port== 443
print(f"Admin: {is_admin}")
print(f"System port: {is_system_port}")
print(f"Web port: {is_web_port}")