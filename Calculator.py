def calculator():
    print("Available operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    while True:
        try:
            choice = input("Enter operation (1/2/3/4/5): ")
            
            if choice == '5':
                print("Exiting calculator...")
                break

            if choice not in ('1', '2', '3', '4'):
                print("Invalid input, please try again.")
                continue

            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            if choice == '1':
                print("{} + {} = {}".format(num1, num2, num1 + num2))
            elif choice == '2':
                print("{} - {} = {}".format(num1, num2, num1 - num2))
            elif choice == '3':
                print("{} * {} = {}".format(num1, num2, num1 * num2))
            elif choice == '4':
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    print("{} / {} = {}".format(num1, num2, num1 / num2))

        except ValueError:
            print("Invalid number input, please enter integers only.")

calculator()
