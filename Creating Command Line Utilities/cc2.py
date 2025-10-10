# 1. Creating the Argument Parser
# argparse.ArgumentParser(): Creates the main parser object that manages the command-line arguments.
# Example usage of creating a parser with description:
import argparse

# Create parser with description
parser = argparse.ArgumentParser(description="Simple calculator program")

# Add arguments
parser.add_argument("num1", type=int, help="First number")
parser.add_argument("num2", type=int, help="Second number")
parser.add_argument("--operation", choices=["add", "sub"], default="add", help="Operation to perform")

# Parse arguments
args = parser.parse_args()

# Perform operation
if args.operation == "add":
    print(args.num1 + args.num2)
else:
    print(args.num1 - args.num2)
# It creates a variable named parser that holds an ArgumentParser object, and gives that parser a description text (“Simple calculator program”) used only for help output.