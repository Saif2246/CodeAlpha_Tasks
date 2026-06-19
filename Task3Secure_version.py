import getpass

username = input("Enter username: ")
password = getpass.getpass("Enter password: ")

stored_user = "admin"
stored_pass = "1234"

if username == stored_user and password == stored_pass:
    print("Login successful")
else:
    print("Login failed")