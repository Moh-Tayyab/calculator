
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operator_input():
    while True:
        operator = input("Enter operator (+, -, *, /): ").strip()
        if operator in ['+', '-', '*', '/']:
            return operator
        else:
            print("Invalid operator. Please choose from +, -, *, /.")

def main():
    print("Welcome to the Professional Calculator!")
    while True:
        num1 = get_number_input("Enter first number: ")
        operator = get_operator_input()
        num2 = get_number_input("Enter second number: ")

        result = None
        try:
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            
            print(f"Result: {num1} {operator} {num2} = {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
