def find_duplicates(numbers):
    """
    Find duplicates in a list of numbers.

    Parameters:
    numbers (list of int): The list of numbers to check.

    Returns:
    list of int: A list containing duplicate numbers.
    """
    duplicates = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j] and numbers[i] not in duplicates:
                duplicates.append(numbers[i])
    return duplicates

def main():
    numbers = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 9, 1]
    duplicates = find_duplicates(numbers)
    print("Duplicate numbers found:", duplicates)

if __name__ == "__main__":
    main()