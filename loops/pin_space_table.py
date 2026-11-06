# Calculate how long it takes to try every possible PIN of 4 to 8 digits.
GUESSES_PER_SECOND = 10
for digits in range(4, 9):
    combinations = 10 ** digits
    seconds = combinations // GUESSES_PER_SECOND
    minutes = seconds // 60
    days = seconds // (24 * 60 * 60)
    print(f"{digits} digits: {combinations} PINs, {minutes} minutes, {days} days")