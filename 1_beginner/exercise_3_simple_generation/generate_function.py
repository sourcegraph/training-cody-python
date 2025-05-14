from datetime import datetime
def greet_user(name):
    """
    Greet a user with their name.

    Parameters:
    name (str): The name of the user.

    Returns:
    str: A greeting message.
    """
    return f"Hello, {name}! Welcome to Cody Training Workshop."

def calculate_age(dob):
    """
    Calculate a person's age based on their date of birth.
    
    Parameters:
    dob (str): Date of birth in DD/MM/YYYY format.
    
    Returns:
    int: The person's age in years.
    """
    # Parse the date of birth
    day, month, year = map(int, dob.split('/'))
    
    # Get current date
    current_date = datetime.now()
    
    # Calculate age
    age = current_date.year - year
    
    # Check if birthday has occurred this year
    if (current_date.month, current_date.day) < (month, day):
        age -= 1
        
    return age

if __name__ == "__main__":
    # Example user name
    user_name = "Moshin"
    
    # Call greet_user to display a greeting message
    print(greet_user(user_name))
    
    # Example date of birth
    birth_date = "15/06/1990"
    age = calculate_age(birth_date)
    print(f"{user_name} is {age} years old.")