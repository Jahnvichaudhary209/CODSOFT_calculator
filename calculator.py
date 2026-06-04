def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def main():
    print("--- Simple Python Calculator ---")
    
    # Get the numbers from the user with basic input validation
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    # Display operation choices
    print("\nAvailable Operations:")
    print("+ : Addition")
    print("- : Subtraction")
    print("* : Multiplication")
    print("/ : Division")
    
    choice = input("\nSelect an operation (+, -, *, /): ").strip()
    
    # Perform calculation based on the operation chosen
    if choice == '+':
        result = add(num1, num2)
        print(f"\nResult: {num1} + {num2} = {result}")
    elif choice == '-':
        result = subtract(num1, num2)
        print(f"\nResult: {num1} - {num2} = {result}")
    elif choice == '*':
        result = multiply(num1, num2)
        print(f"\nResult: {num1} * {num2} = {result}")
    elif choice == '/':
        result = divide(num1, num2)
        print(f"\nResult: {result}")
    else:
        print("\nInvalid operation symbol selected.")

if __name__ == "__main__":
    main()
