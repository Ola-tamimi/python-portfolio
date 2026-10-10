# fix_the_record.py
# This program prints a short record about a network device.
device_name = "edge-router"
#syntax error
second_ip = "192.0.2.1"
#syntax error
class_ = "router"
#runtime error
port = int("22")
#runtime error
print("Device:", device_name)
print("Backup IP:", second_ip)
print("Type:", class_)
print("Port:", port)
# Python reports Syntax Errors first because it checks the code syntax before execution. Runtime Errors appear during execution.