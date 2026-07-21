def login():
    attempt = 1

    while attempt <= 3:

     username = input("Enter username: ")
     password = input("Eneter password: ")

     if username == "admin" and password == "1234":
        print("Access Granted")
        break

     else:
        print("Access Denied")
        attempt = attempt + 1

        if attempt > 3:
           print("Too many failed login attempt.")
        

print("===== Enterprise SOC login System =====")
login()