# Classify port numbers, check passwords, and estimate PIN guessing time.
MIN_LENGTH=8
def border(width):
    """Print the top or bottom border of a box."""
    print("+" + "-" * (width + 2) + "+")


def show_box(text):
    """Print text inside a box."""
    width = len(text)
    border(width)
    print(f"| {text} |")
    border(width)

def show_menu():
    """Print the toolkit menu."""
    print("SECURITY TOOLKIT")
    print("1. Check a port")
    print("2. Check a password")
    print("3. PIN guessing time")
    print("q. Quit")

def port_range(port):
    """Return the category of a port number."""
    if port < 0 or port > 65535:
        return "invalid"
    if port <= 1023:
        return "system"
    if port <= 49151:
        return "user"
    return "dynamic"

def check_port():
    """Read a port number and display its category."""
    port = int(input("Port: "))
    category = port_range(port)
    show_box(f"Port {port}: {category}")

def password_problem(password, username):
    """Return the first password problem or an empty string."""
    if len(password) < MIN_LENGTH:
        return f"too short (at least {MIN_LENGTH})"
    if password == username:
        return "same as the username"
    return ""

def check_password():
    """Read a username and password and display the result."""
    username = input("Username: ")
    password = input("Password: ")
    problem = password_problem(password, username)

    if problem:
        show_box(f"Rejected: {problem}")
    else:
        show_box("Password accepted")

def days_to_guess(digits, per_second):
    """Return the whole days needed to try every possible PIN."""
    return 10 ** digits // per_second // 86400

def check_pin():
    """Read the PIN length and guessing rate and display the estimate."""
    digits = int(input("PIN digits: "))
    per_second = int(input("Guesses per second: "))
    days = days_to_guess(digits, per_second)
    show_box(f"{digits} digits: {days} days")

show_menu()
checks_done = 0

while True:
    choice = input("Choice (1, 2, 3, or q): ")

    if choice == "1":
        check_port()
    elif choice == "2":
        check_password()
    elif choice == "3":
        check_pin()
    elif choice == "q":
        break
    else:
        print("Unknown choice.")
        continue

    checks_done += 1

show_box(f"Checks done: {checks_done}")