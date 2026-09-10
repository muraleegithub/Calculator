#!/usr/bin/env python3
"""
Simple interactive calculator (add, subtract, multiply, divide, power, remainder).
Menu accepts either numbers (1-8) or operator symbols (+ - * / ^ % # $).
"""
import sys

def perform_operation(choice: str, a: float, b: float):
    """Perform the requested operation and return a result string."""
    try:
        if choice in ("1", "+"):
            return f"{a} + {b} = {a + b}"
        if choice in ("2", "-"):
            return f"{a} - {b} = {a - b}"
        if choice in ("3", "*"):
            return f"{a} * {b} = {a * b}"
        if choice in ("4", "/"):
            if b == 0:
                return "Error: Division by zero"
            return f"{a} / {b} = {a / b}"
        if choice in ("5", "^"):
            return f"{a} ^ {b} = {a ** b}"
        if choice in ("6", "%"):
            if b == 0:
                return "Error: Remainder by zero"
            return f"{a} % {b} = {a % b}"
    except Exception as e:
        return f"Error performing operation: {e}"
    return "Unknown operation"

def get_number(prompt: str):
    """Prompt repeatedly until we get a valid number or user cancels (EOF)."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled. Terminating.")
            sys.exit(0)

def main():
    while True:
        print("\nSelect operation.")
        print("1.Add      : + ")
        print("2.Subtract : - ")
        print("3.Multiply : * ")
        print("4.Divide   : / ")
        print("5.Power    : ^ ")
        print("6.Remainder: % ")
        print("7.Terminate: # ")
        print("8.Reset    : $ ")

        choice = input("Enter choice (1/2/3/4/5/6/7/8 or + - * / ^ % # $): ").strip()
        if not choice:
            print("No input — try again.")
            continue

        # Terminate
        if choice in ("7", "#"):
            print("Done. Terminating.")
            break

        # Reset (just restarts the loop)
        if choice in ("8", "$"):
            print("Resetting...")
            continue

        # Valid operation: get operands then perform
        if choice in ("1","2","3","4","5","6","+","-","*","/","^","%"):
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            result = perform_operation(choice, a, b)
            print(result)
            continue

        print(f"'{choice}' is not a valid operator. Please try again.")

if __name__ == "__main__":
    main()
