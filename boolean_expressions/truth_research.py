
# Source: https://docs.python.org/3/library/stdtypes.html#truth-value-testing

# bool("") is False because the string is empty.
print(bool(""))

# bool("0") is True because the string is not empty.
print(bool("0"))

# bool(0) is False because zero is considered False.
print(bool(0))

# bool(0.0) is False because it is a numeric zero.
print(bool(0.0))

# bool("False") is True because the string is not empty.
print(bool("False"))
