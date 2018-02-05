def password_function():
    name = input("Enter username: ")
    if name == "Zoe":
        password = input("Enter password: ")
        if password == "Hi":
            print("welcome")
        else:
            print("Incorrect")
    else:
        print("Access denied")
