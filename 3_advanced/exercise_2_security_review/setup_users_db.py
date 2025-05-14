import sqlite3

def setup_database():
    # Connect to SQLite database (it will create it if it doesn't exist)
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    # Create table 'users' if it does not exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id TEXT PRIMARY KEY,
        name TEXT,
        email TEXT
    )
    ''')

    # Create table 'orders' if it does not exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT NOT NULL,
        item_price REAL NOT NULL,
        owner_id TEXT NOT NULL,
        FOREIGN KEY (owner_id) REFERENCES users(id)
    )
    ''')

    # Insert example users
    example_users = [
        ('0', 'Moshin', 'moshin@example.com'),
        ('1', 'Lee', 'moshin@example.com'),
        ('2', 'Bob', 'bob@example.com'),
        ('3', 'Charlie', 'charlie@example.com')
    ]

    # Delete existing records to ensure fresh insert
    cursor.execute('DELETE FROM users')
    
    # Insert example records
    cursor.executemany('INSERT INTO users (id, name, email) VALUES (?, ?, ?)', example_users)
    
    # Insert example orders
    example_orders = [
        ('Book', 19.99, '0'),
        ('Laptop', 999.99, '0'),
        ('Headphones', 89.99, '1'),
        ('Phone Case', 15.99, '2'),
        ('Monitor', 299.99, '2'),
        ('Keyboard', 59.99, '3')
    ]
    
    # Delete existing orders to ensure fresh insert
    cursor.execute('DELETE FROM orders')
    
    # Insert example orders
    cursor.executemany('INSERT INTO orders (item_name, item_price, owner_id) VALUES (?, ?, ?)', example_orders)
    
    # Commit changes and close the connection
    connection.commit()
    connection.close()

if __name__ == "__main__":
    setup_database()
    print("Database setup complete with example users and orders.")