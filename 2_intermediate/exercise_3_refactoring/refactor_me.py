def process_data(data):
    """
    Processes a list of numbers by filtering, transforming, and aggregating.
    """
    # Step 1: Filter out negative numbers
    filtered_data = []
    for item in data:
        if item >= 0:
            filtered_data.append(item)
    
    # Step 2: Square each number
    squared_data = []
    for item in filtered_data:
        squared_data.append(item * item)
    
    # Step 3: Sum all the squared numbers
    total = 0
    for item in squared_data:
        total += item
    
    return total

if __name__ == "__main__":
    sample_data = [1, -2, 3, 4, -5]
    print("Processed data result:", process_data(sample_data))