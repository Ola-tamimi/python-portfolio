# risk_score.py
# Calculate and classify login risk.
score = 0
failed = int(input("Failed attempts: "))
hour = int(input("Login hour (0-23): "))
new_device = input("New device (yes/no): ")

# Add risk points
if failed >= 3:
    score += 40

if hour < 6:
    score += 30

if new_device == "yes":
    score += 30

# Classify risk level
if score >= 70:
    level = "HIGH"
elif score >= 30:
    level = "MEDIUM"
else:
    level = "LOW"

print(f"Risk score: {score} ({level})")

