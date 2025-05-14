import sqlite3

def get_user_data(user_id):
    """
    Fetches user data from the database by user_id.

    Parameters:
    user_id (str): The ID of the user.

    Returns:
    str: User data in a simple format.
    """
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    # Vulnerability: SQL Injection
    query = f"SELECT * FROM users WHERE id='{user_id}'"
    cursor.execute(query)

    result = cursor.fetchone()
    connection.close()

    # Vulnerability: Insecure data handling
    if result:
        return f"User Data: {result}"
    else:
        return "No user found."

def main():
    user_id = input("Enter user ID: ")
    
    # Vulnerability: Unvalidated user input
    print(get_user_data(user_id))

if __name__ == "__main__":
    main()