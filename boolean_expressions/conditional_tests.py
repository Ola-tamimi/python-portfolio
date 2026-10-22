user="analyst"
role="viewer"
failed=3
port=22
# Test 1
print("Is failed >= 3? I predict True.")
print(failed >= 3)

# Test 2
print("\nIs role == admin? I predict False.")
print(role == "admin")

# Test 3
print("\nIs port != 23? I predict True.")
print(port != 23)

# Test 4
print("\nIs failed > 5? I predict False.")
print(failed > 5)

# Test 5
print("\nIs port < 30? I predict True.")
print(port < 30)

# Test 6
print("\nIs failed <= 2? I predict False.")
print(failed <= 2)

# Test 7
print("\nIs user == analyst and port == 22? I predict True.")
print(user == "analyst" and port == 22)

# Test 8
print("\nIs role == admin or failed > 5? I predict False.")
print(role == "admin" or failed > 5)

# Test 9
print("\nIs not (role == admin)? I predict True.")
print(not (role == "admin"))

# Test 10
print("\nIs port < 20 and failed == 3? I predict False.")
print(port < 20 and failed == 3)
