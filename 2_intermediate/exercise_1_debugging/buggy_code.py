def divide_numbers(num1, num2):
    """
    Divide two numbers and return the result.

    Parameters:
    num1 (float): The numerator.
    num2 (float): The denominator.

    Returns:
    float: The result of the division.
    """
    result = num1 / num2  # Debug error: Ensure num2 is not zero
    return result

def main():
    """
    Main function to test divide_numbers.
    """
    # Test cases
    numbers = [(10, 2), (5, 0), (9, 3)]

    for num1, num2 in numbers:
        print(f"Dividing {num1} by {num2} gives {divide_numbers(num1, num2)}")

if __name__ == "__main__":
    # There's an intentional bug here - division by zero
    # Additional bug - error handling needs to be added
    main()