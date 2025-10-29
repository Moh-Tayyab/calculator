# Calculator Project

A simple command-line calculator application built with Python. This project demonstrates basic arithmetic operations and provides an interactive interface for user input.

## Features

*   **Interactive Interface:** Users can input two numbers and select an arithmetic operator.
*   **Integer Operations:** The calculator is designed to work with integer inputs and provides integer results (division results are truncated).
*   **Addition:** Add two numbers.
*   **Subtraction:** Subtract one number from another.
*   **Multiplication:** Multiply two numbers.
*   **Division:** Divide one number by another, with error handling for division by zero.

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
    This will create a virtual environment.

## How to Run

To run the interactive calculator:

1.  **Activate the virtual environment:**
    ```bash
    .\.venv\Scripts\Activate.ps1  # On Windows PowerShell
    # source .venv/bin/activate   # On Linux/macOS
    ```

2.  **Execute the main script:**
    ```bash
    python main.py
    ```
    The calculator will then prompt you to enter numbers and select an operator.

## Usage Examples

When you run `python main.py`, you will be prompted as follows:

```
Welcome to the Professional Calculator!
Enter first number: 10
Enter operator (+, -, *, /): +
Enter second number: 5
Result: 10 + 5 = 15
Do you want to perform another calculation? (yes/no): yes
Enter first number: 10
Enter operator (+, -, *, /): /
Enter second number: 3
Result: 10 / 3 = 3  # Note: Result is truncated to an integer
Do you want to perform another calculation? (yes/no): no
Thank you for using the calculator. Goodbye!
```