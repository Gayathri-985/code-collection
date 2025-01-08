# Custom exception
class NegativeValueError(Exception):
    def __init__(self, message="Negative values are not allowed"):
        self.message = message
        super().__init__(self.message)

# Function to divide two numbers
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Invalid input type. Please provide numbers.")
        return None
    else:
        print(f"The result of division is: {result}")
        return result
    finally:
        print("Execution of divide_numbers is complete.")

# Function to calculate square root
import math
def calculate_square_root(value):
    try:
        if value < 0:
            raise NegativeValueError("Square root of a negative number is not defined.")
        result = math.sqrt(value)
    except NegativeValueError as e:
        print(f"Error: {e}")
    except TypeError:
        print("Error: Input must be a number.")
    else:
        print(f"The square root of {value} is: {result}")
    finally:
        print("Execution of calculate_square_root is complete.")

# Function to demonstrate exception hierarchy
def exception_hierarchy_demo():
    try:
        # Uncomment one of the following lines to trigger different exceptions
        # x = int("not a number")  # ValueError
        # y = undefined_variable   # NameError
        # z = [1, 2, 3][5]         # IndexError
        pass
    except (ValueError, NameError, IndexError) as e:
        print(f"Error occurred: {e}")
    finally:
        print("Execution of exception_hierarchy_demo is complete.")

# Main program
if __name__ == "__main__":
    print("Error and Exception Handling Example\n")

    # Handling division
    divide_numbers(10, 0)  # ZeroDivisionError
    divide_numbers(10, "5")  # TypeError
    divide_numbers(10, 5)  # Valid case

    print("\n")

    # Handling square root calculation
    calculate_square_root(-9)  # NegativeValueError
    calculate_square_root("16")  # TypeError
    calculate_square_root(16)  # Valid case

    print("\n")

    # Demonstrating exception hierarchy
    exception_hierarchy_demo()
