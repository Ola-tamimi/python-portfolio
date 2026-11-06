# Count failed logins and calculate the average session length.

events = ["FAILED", "SUCCESS", "FAILED", "SUCCESS", "SUCCESS"]
minutes = [0, 30, 0, 15, 45]

# Fix 1: Initialize the counter before the loop so it does not reset on each pass.
failed = 0
for event in events:
    if event == "FAILED":
        failed += 1

print(f"Failed logins: {failed}")

total = 0
count = 0
for value in minutes:
    if value > 0:
        total += value
        count += 1

# Fix 2: Use / to get a decimal result such as 30.0.
average = total / count

# Fix 3: Print after the loop so the final average appears only once.
print(f"Average session: {average} minutes")

# Fix 4: Use 5 as the stop value because range does not include it.
for level in range(1, 5):
    print(f"Level {level}")