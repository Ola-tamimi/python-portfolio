# fix_the_functions.py
def print_header():
    """Display the report header."""
    print("=" * 30)
    print("LOGIN REPORT")
    print("=" * 30)
def lock_minutes(failed, minutes=15):
    """Return failed * minutes if failed >= 3, else 0."""
    if failed >= 3:
        total = failed * minutes
        # semantic: Return the calculated lock time.
        return total
    return 0
def login_line(username, failed):
    """Return one line of the report."""
    minutes = lock_minutes(failed)
    return f"{username}: {failed} failed, locked {minutes} min"
# runtime: Call the function after it is defined.
print_header()
# runtime: Use the correct parameter name.
print(login_line(username="sara", failed=4))
# semantic: Print the returned report line.
print(login_line("omar", 1))