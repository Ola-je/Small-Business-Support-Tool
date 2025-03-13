import sqlite3



# Function to establish a database connection
def get_db_connection():
    connection = sqlite3.connect("app.db")
    connection.row_factory = sqlite3.Row  # To access rows as dictionaries
    return connection
# connection = get_db_connection()
# cursor = connection.cursor()
# cursor.execute(f"DROP TABLE IF EXISTS inventory")
# connection.commit()
# connection.close()
# print(f"Table 'inventory' has been dropped (if it existed).")
# Function to initialize the database
def init_db():
    connection = get_db_connection()
    cursor = connection.cursor()

    # Create table and index
    cursor.executescript("""
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
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


#create basic functionality 
# create ,update the itemquantity

# def create_new_item(itemNmae,itemQuantity,price,suplierName,catagory):
#     connection= get_db_connection()
#     cursor=connection.cursor
#     cursor.execute("""
# INSER INTO inventory (iteamName,itesmQuantity,price,suplierName,catagory) VALUE(?,?,?,?)
# """

#     )

def create_item(item_name, item_quantity, price, supplier_name, category):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO inventory (itemName, itemQuantity, price, supplierName, category)
        VALUES (?, ?, ?, ?, ?)
    """, (item_name, item_quantity, price, supplier_name, category))
    connection.commit()
    connection.close()


def get_all_items():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM inventory")
    rows = cursor.fetchall()
    connection.close()
    return [dict(row) for row in rows]  # Convert rows to dictionaries


def get_item_by_name(item_name):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM inventory WHERE itemName = ?", (item_name,))
    row = cursor.fetchone()
    connection.close()
    return dict(row) if row else None
def update_item(item_name, item_quantity=None, price=None):
    connection = get_db_connection()
    cursor = connection.cursor()

    # Fetch the current values to use as defaults if none are provided
    cursor.execute("SELECT itemQuantity, price FROM inventory WHERE itemName = ?", (item_name,))
    row = cursor.fetchone()

    if not row:
        connection.close()
        raise ValueError(f"Item with name '{item_name}' does not exist")

    current_quantity, current_price = row

    # Use provided values or fallback to existing ones
    new_quantity = item_quantity if item_quantity is not None else current_quantity
    new_price = price if price is not None else current_price

    # Execute the update query
    cursor.execute("""
        UPDATE inventory
        SET itemQuantity = ?, price = ?
        WHERE itemName = ?
    """, (new_quantity, new_price, item_name))

    connection.commit()
    connection.close()

def delete_item(item_name):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM inventory WHERE itemName = ?", (item_name,))
    connection.commit()
    connection.close()


create_item("Laptop", 10, 1500.00, "Tech Supplier", "Electronics")
create_item("Headphones", 50, 200.00, "AudioWorld", "Accessories")

# Test getting all items
items = get_all_items()
print("All Items:", items)

# Test getting a specific item by name
item = get_item_by_name("Laptop")
print("Laptop Details:", item)

# Test updating an item
update_item("Laptop", item_quantity=15)  # Update quantity only
updated_item = get_item_by_name("Laptop")
print("Updated Laptop:", updated_item)

# Test deleting an item
delete_item("Headphones")
items_after_deletion = get_all_items()
print("Items After Deletion:", items_after_deletion)
