def calculator():
    """
    Simple calculator that performs basic arithmetic operations on two numbers.
    """
    print("=" * 50)
    print("WELCOME TO THE CALCULATOR")
    print("=" * 50)
    
    # Get first number from user
    while True:
        try:
            num1 = float(input("\nEnter the first number: "))
            break
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
    
    # Get second number from user
    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
    
    # Display operation menu
    print("\n" + "-" * 50)
    print("Choose an arithmetic operation:")
    print("-" * 50)
    print("1. Plus (Addition)")
    print("2. Substracción (Subtraction)")
    print("3. Times by (Multiplication)")
    print("4. Divided by (Division)")
    print("-" * 50)
    
    # Get user's choice
    while True:
        operation = input("\nEnter your choice (1, 2, 3, or 4): ").strip()
        if operation in ['1', '2', '3', '4']:
            break
        else:
            print("❌ Invalid choice! Please enter 1, 2, 3, or 4.")
    
    # Perform the selected operation
    if operation == '1':
        result = num1 + num2
        operation_name = "Plus"
        symbol = "+"
    elif operation == '2':
        result = num1 - num2
        operation_name = "Substracción"
        symbol = "-"
    elif operation == '3':
        result = num1 * num2
        operation_name = "Times by"
        symbol = "*"
    elif operation == '4':
        if num2 == 0:
            print("\n❌ Error: Cannot divide by zero!")
            return
        result = num1 / num2
        operation_name = "Divided by"
        symbol = "/"
    
    # Display the result
    print("\n" + "=" * 50)
    print("CALCULATION RESULT")
    print("=" * 50)
    print(f"{num1} {symbol} {num2} = {result}")
    print(f"\nOperation: {operation_name}")
    print("=" * 50)


if __name__ == "__main__":
    calculator()
    
    # Ask if user wants to perform another calculation
    while True:
        again = input("\nWould you like to perform another calculation? (yes/no): ").strip().lower()
        if again in ['yes', 'y']:
            print("\n")
            calculator()
        elif again in ['no', 'n']:
            print("\nThank you for using the calculator! Goodbye! 👋")
            break
        else:
            print("❌ Invalid input! Please enter 'yes' or 'no'.")
