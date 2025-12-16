"""
Calculator CLI - Command Line Interface for the Calculator
"""

import calculator


def print_menu():
    """Display the calculator menu."""
    print("\n=== Simple Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulo")
    print("0. Exit")
    print("=" * 25)


def get_number(prompt):
    """
    Get a number from user input.
    
    Args:
        prompt (str): Prompt message
    
    Returns:
        float: User input as a number
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    """Main function to run the calculator."""
    print("Welcome to the Simple Calculator!")
    
    while True:
        print_menu()
        choice = input("Enter your choice (0-6): ")
        
        if choice == "0":
            print("Thank you for using the calculator. Goodbye!")
            break
        
        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice. Please try again.")
            continue
        
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        
        try:
            if choice == "1":
                result = calculator.add(num1, num2)
                print(f"\n{num1} + {num2} = {result}")
            elif choice == "2":
                result = calculator.subtract(num1, num2)
                print(f"\n{num1} - {num2} = {result}")
            elif choice == "3":
                result = calculator.multiply(num1, num2)
                print(f"\n{num1} × {num2} = {result}")
            elif choice == "4":
                result = calculator.divide(num1, num2)
                print(f"\n{num1} ÷ {num2} = {result}")
            elif choice == "5":
                result = calculator.power(num1, num2)
                print(f"\n{num1} ^ {num2} = {result}")
            elif choice == "6":
                result = calculator.modulo(num1, num2)
                print(f"\n{num1} % {num2} = {result}")
        except ValueError as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()
