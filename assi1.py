
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nBasic Calculations")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Addition =", num1 + num2)

    elif choice == "2":
        print("Subtraction =", num1 - num2)

    elif choice == "3":
        print("Multiplication =", num1 * num2)

    elif choice == "4":
        if num2 != 0:
            print("Division =", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")

    else:
        print("Invalid choice!")

    # Optional advanced calculations
    advanced = input("\nDo you want advanced calculations? (yes/no): ")

    if advanced.lower() == "yes":
        print("\nAdvanced Calculations")
        print("1. Exponentiation")
        print("2. Modulus")

        hard_choice = input("Enter your choice (1-2): ")

        if hard_choice == "1":
            print("Exponentiation =", num1 ** num2)

        elif hard_choice == "2":
            if num2 != 0:
                print("Modulus =", num1 % num2)
            else:
                print("Error: Modulus by zero is not allowed.")

        else:
            print("Invalid advanced choice!")

    elif advanced.lower() != "no":
        print("Invalid input! Please enter yes or no.")

except ValueError:
    print("Error: Please enter valid numbers and choices.")

except OverflowError:
    print("Error: The result is too large.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
