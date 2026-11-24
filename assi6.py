
while True:
    password = input("Enter a password (or type 'stop' to exit): ")

    if password.lower() == "stop":
        print("Program stopped.")
        break

    # Check password criteria
    if (len(password) >= 8
            and any(char.isupper() for char in password)
            and any(char.islower() for char in password)
            and any(char.isdigit() for char in password)):

        print("Strong password!")
    else:
        print("Weak password!")
