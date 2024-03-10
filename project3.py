try:
    username = input("Enter username: ")
    password = input("Enter password: ")
except ValueError:
    print('Please enter a valid value.')

if username == "admin" and password == "admin":
    print("Successfully logged in.")
else:
    print("Wrong username or password.")
