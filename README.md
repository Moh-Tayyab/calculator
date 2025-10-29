# Calculator Project

A simple command-line calculator application built with Python. This project demonstrates basic arithmetic operations and includes unit tests for functionality verification.

## Features

*   **Addition:** Add two numbers.
*   **Subtraction:** Subtract one number from another.
*   **Multiplication:** Multiply two numbers.
*   **Division:** Divide one number by another, with error handling for division by zero.
*   **Unit Tests:** Comprehensive tests for all arithmetic operations using `pytest`.

## Installation

To set up the project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Moh-Tayyab/calculator.git
    cd calculator
    ```

2.  **Install dependencies using `uv`:**
    This project uses `uv` for dependency management. If you don't have `uv` installed, you can install it via `pip`:
    ```bash
    pip install uv
    ```
    Then, install the project dependencies:
    ```bash
    uv pip install .
    ```
    This will create a virtual environment and install `pytest`.

## How to Run

You can interact with the calculator functions directly in a Python interpreter.

1.  **Activate the virtual environment:**
    ```bash
    .\.venv\Scripts\Activate.ps1  # On Windows PowerShell
    # source .venv/bin/activate   # On Linux/macOS
    ```

2.  **Start the Python interpreter:**
    ```bash
    python
    ```

3.  **Import and use the calculator functions:**
    ```python
    from src.calculator import add, subtract, multiply, divide

    # Example Usage:
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"10 / 2 = {divide(10, 2)}")

    try:
        divide(1, 0)
    except ValueError as e:
        print(f"Error: {e}")
    ```

## How to Run Tests

The project includes unit tests using `pytest`.

1.  **Activate the virtual environment:**
    ```bash
    .\.venv\Scripts\Activate.ps1  # On Windows PowerShell
    # source .venv/bin/activate   # On Linux/macOS
    ```

2.  **Run the tests:**
    ```bash
    pytest
    ```

    You should see output indicating that all tests passed.

## Usage Examples

Here are some examples of how to use the calculator functions:

```python
from src.calculator import add, subtract, multiply, divide

result_add = add(15, 7)  # 22
result_subtract = subtract(20, 8) # 12
result_multiply = multiply(4, 9) # 36
result_divide = divide(100, 10) # 10.0

print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")
print(f"Multiplication: {result_multiply}")
print(f"Division: {result_divide}")

# Division by zero error handling
try:
    divide(5, 0)
except ValueError as e:
    print(f"Caught error: {e}")
```