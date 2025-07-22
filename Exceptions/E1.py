try:
    # Code that may raise an exception
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)

# ValueError it is buit-in exception for invalid literal for int()
except ValueError:
    # This block runs if there's a ValueError, e.g., if input is not an integer
    print("Invalid input! Please enter a valid number.")

# ZeroDivisionError it is buit-in exception for division by zero

except ZeroDivisionError:
    # This block runs if the user tries to divide by zero
    print("Error! Division by zero is not allowed.")

# Exception it is a general exception that catches all other exceptions
except Exception as e:
    # General exception to catch any other types of errors
    print(f"An unexpected error occurred: {e}")

# Finally block runs regardless of whether an exception occurred or not
finally:
    # This block always runs, whether or not there was an exception
    print("Execution completed.")