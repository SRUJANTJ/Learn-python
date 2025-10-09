# example.py
import argparse

parser = argparse.ArgumentParser(description="Example command line utility")

# Positional arguments
parser.add_argument("arg1", help="Description of argument 1")
parser.add_argument("arg2", help="Description of argument 2")

# Parse the arguments
args = parser.parse_args()

# Use the arguments
print("Argument 1:", args.arg1)
print("Argument 2:", args.arg2)


# to run this script from the command line:
#  python cc1.py hello world