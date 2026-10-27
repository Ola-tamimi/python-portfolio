port=int(input("Enter a port:"))
if port<0 or port>65535:
    print("Invalid port: use a number from 0 to 65535")
elif port==22:
    print("Range:system")
    print("service:ssh")
elif port==80:
    print("Range:system")
    print("service:http")
elif port==443:
     print("Range:system")
     print("service:https")    
elif port>=0 and port<=1023:
    print("Range:system")
elif port>=1024 and port<=49151:
    print("Range:user")
else:
    print("Range: dynamic or private")

