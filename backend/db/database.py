import sqlite3

# Function to establish a database connection
def get_db_connection():
    connection = sqlite3.connect("./app.db")
    connection.row_factory = sqlite3.Row  # To access rows as dictionaries
    return connection

# Function to initialize the database
def init_db():
    connection = get_db_connection()
    cursor = connection.cursor()

    # Create table and index
    cursor.executescript("""
CREATE TABLE IF NOT EXISTS inventory (
    id INT PRIMARY KEY,
    itemName TEXT NOT NULL,
    itemQuantity INT NOT NULL DEFAULT 0 CHECK (itemQuantity >= 0),
    price DECIMAL(10, 2) NOT NULL DEFAULT 0.00 CHECK (price >= 0),
    createdTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updatedTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    stockStatus TEXT DEFAULT 'In Stock' CHECK (stockStatus IN ('In Stock', 'Out of Stock')),
    supplierName TEXT,
    category TEXT NOT NULL DEFAULT 'Uncategorized'
);

CREATE TRIGGER IF NOT EXISTS update_updatedTime
AFTER UPDATE ON inventory
FOR EACH ROW
BEGIN
    UPDATE inventory SET updatedTime = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;
""")


    connection.commit()
    connection.close()

# Call this function whenever you want to initialize or reset the database
if __name__ == "__main__":
    init_db()
    print("Database and table initialized successfully.")
