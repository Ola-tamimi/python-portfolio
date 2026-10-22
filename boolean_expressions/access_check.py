MAX_FAILED = 5

role = input("Role: ")
mfa = input("MFA passed (yes/no): ")
failed = int(input("Failed attempts: "))

mfa_ok = mfa == "yes"
is_privileged = role == "admin" or role == "root"
can_log_in = mfa_ok and failed < MAX_FAILED

print(f"Privileged role: {is_privileged}")
print(f"MFA OK: {mfa_ok}")
print(f"Can log in: {can_log_in}")
