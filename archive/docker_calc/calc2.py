import argparse
import sys

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def get_sum(self):
        return self.num1 + self.num2

    def get_difference(self):
        return self.num1 - self.num2

    def get_product(self):
        return self.num1 * self.num2

    def get_quotient(self):
        return self.num1 / self.num2

def prompt_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def prompt_operation():
    operations = ["sum", "diff", "prod", "quot"]
    while True:
        op = input(f"Enter operation ({', '.join(operations)}): ").strip().lower()
        if op in operations:
            return op
        print("Invalid operation. Please try again.")



def parse_args():
    parser = argparse.ArgumentParser(description="Calculator CLI")
    parser.add_argument("--num1", type=float,  help="First operand")
    parser.add_argument("--num2", type=float,  help="Second operand")
    parser.add_argument("--op",choices=["sum", "diff", "prod", "quot"],help="Operation to perform")

    return parser.parse_args()

def main():
    print("Welcome to the Calculator CLI! You know you can do this on your phone yeah?")

    args = parse_args()
    interactive = sys.stdin.isatty()

    # If no CLI arguments AND not interactive, warn user
    if args.num1 is None and args.num2 is None and not interactive:
        print("\nYou forgot your arguments! 🫣")
        print('Hint: Either run with CLI args like "--num1 10 --num2 2 --op sum"')
        print('      Or run interactively with Docker: "docker run -it mycalc"')
        return

    # Get numbers
    if args.num1 is not None:
        num1 = args.num1
    elif interactive:
        num1 = prompt_float("Enter first number: ")
    else:
        # Should never reach here because of the previous check
        return

    if args.num2 is not None:
        num2 = args.num2
    elif interactive:
        num2 = prompt_float("Enter second number: ")
    else:
        return

    # Get operation
    op = args.op if args.op is not None else (prompt_operation() if interactive else "sum")

    calc = Calculator(num1, num2)

    if op == "sum":
        print(calc.get_sum())
    elif op == "diff":
        print(calc.get_difference())
    elif op == "prod":
        print(calc.get_product())
    elif op == "quot":
        if num2 == 0:
            print("Nah then, stop tryin to bust it: Division by zero is not allowed.")
        else:
            print(calc.get_quotient())
if __name__ == "__main__":
    main()