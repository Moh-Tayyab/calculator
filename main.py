
# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    # Check for division by zero to prevent errors
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Function to get a valid number input from the user
def get_number_input(prompt):
    while True:
        try:
            # Attempt to convert input to an integer
            return int(input(prompt))
        except ValueError:
            # Handle cases where input is not a valid integer
            print("Invalid input. Please enter an integer.")

# Function to get a valid operator input from the user
def get_operator_input():
    while True:
        # Get operator input and remove leading/trailing whitespace
        operator = input("Enter operator (+, -, *, /): ").strip()
        # Check if the operator is one of the allowed operations
        if operator in ['+', '-', '*', '/']:
            return operator
        else:
            # Inform the user about invalid operator input
            print("Invalid operator. Please choose from +, -, *, /.")

# Main function to run the calculator application
def main():
    print("Welcome to the Professional Calculator!")
    # Loop indefinitely to allow multiple calculations
    while True:
        # Get the first number from the user
        num1 = get_number_input("Enter first number: ")
        # Get the operator from the user
        operator = get_operator_input()
        # Get the second number from the user
        num2 = get_number_input("Enter second number: ")

        result = None
        try:
            # Perform the calculation based on the chosen operator
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            
            # Print the result, ensuring it's an integer
            print(f"Result: {num1} {operator} {num2} = {int(result)}")
        except ValueError as e:
            # Handle specific errors like division by zero
            print(f"Error: {e}")
        except Exception as e:
            # Handle any other unexpected errors
            print(f"An unexpected error occurred: {e}")

        # Ask the user if they want to perform another calculation
        another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        # Exit the loop if the user does not want to continue
        if another_calculation != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

# Entry point of the script
if __name__ == "__main__":
    main()
