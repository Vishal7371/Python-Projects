def show_menu():
    print("A calculator made by Vishal!!")
    print("What type of calculation do you want to do?")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
def get_user_input():
    operation = int(input("Enter the number corresponding to the calculation you want to do: "))
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return operation, num1, num2

# Functions for operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b 

def multiplication(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero is not allowed.."

def calculate(operation, num1, num2):
    if operation == 1:
        return add(num1, num2)
    elif operation == 2:
        return subtract(num1, num2)
    elif operation == 3:
        return multiplication(num1, num2)
    elif operation == 4:
        return divide(num1, num2)
    else:
        return "Invalid Operation!!!!"

# Integrate all components
def main():
    show_menu()
    operation, num1, num2 = get_user_input()
    result = calculate(operation, num1, num2)
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
