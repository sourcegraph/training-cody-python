def add(a, b):
    """
    Add two numbers.

    Parameters:
    a (int): First number.
    b (int): Second number.

    Returns:
    int: The sum of a and b.
    """
    return a + b

def multiply(a, b):
    """
    Multiply two numbers.

    Parameters:
    a (int): First number.
    b (int): Second number.

    Returns:
    int: The product of a and b.
    """
    return a * b

if __name__ == "__main__":
    # Example code to demonstrate usage
    print(f"Adding 2 and 3 gives {add(2, 3)}")
    print(f"Multiplying 2 and 3 gives {multiply(2, 3)}")