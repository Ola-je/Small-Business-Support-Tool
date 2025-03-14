# # import sqlite3
# # import os
# # # Function to establish a database connection
# # def get_db_connection():
# #     # Get the absolute path to the 'db' folder
# #     db_path = os.path.join(os.path.dirname(__file__), 'app.db')  # Adjusted to db/app.db
# #     connection = sqlite3.connect(db_path)
# #     connection.row_factory = sqlite3.Row
# #     return connection




# # # connection = get_db_connection()
# # # cursor = connection.cursor()
# # # cursor.execute(f"DROP TABLE IF EXISTS inventory")
# # # connection.commit()
# # # connection.close()
# # # print(f"Table 'inventory' has been dropped (if it existed).")
# # # Function to initialize the database
# # def init_db():
# #     connection = get_db_connection()
# #     cursor = connection.cursor()

# #     # Create table and index
# #     cursor.executescript("""
# # CREATE TABLE IF NOT EXISTS inventory (
# #     id INTEGER PRIMARY KEY AUTOINCREMENT,
# #     itemName TEXT NOT NULL,
# #     itemQuantity INT NOT NULL DEFAULT 0 CHECK (itemQuantity >= 0),
# #     price DECIMAL(10, 2) NOT NULL DEFAULT 0.00 CHECK (price >= 0),
# #     createdTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# #     updatedTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# #     stockStatus TEXT DEFAULT 'In Stock' CHECK (stockStatus IN ('In Stock', 'Out of Stock')),
# #     supplierName TEXT,
# #     category TEXT NOT NULL DEFAULT 'Uncategorized'
# # );

# # CREATE TRIGGER IF NOT EXISTS update_updatedTime
# # AFTER UPDATE ON inventory
# # FOR EACH ROW
# # BEGIN
# #     UPDATE inventory SET updatedTime = CURRENT_TIMESTAMP WHERE id = OLD.id;
# # END;
# #                          CREATE TABLE IF NOT EXISTS transactions (
# #     id INTEGER PRIMARY KEY AUTOINCREMENT,
# #     transactionType TEXT CHECK(transactionType IN ('Income', 'Expense')) NOT NULL,
# #     amount REAL NOT NULL CHECK(amount >=0),
# #     category TEXT NOT NULL,
# #     description TEXT,
# #     transactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
# #     updatedTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# #     relatedInventoryId INTEGER,
# #     FOREIGN KEY (relatedInventoryId) REFERENCES inventory(id)
# # );
# # CREATE TRIGGER IF NOT EXISTS update_updatedTime
# # AFTER UPDATE ON transactions
# # FOR EACH ROW
# # BEGIN
# #     UPDATE transactions SET updatedTime = CURRENT_TIMESTAMP WHERE id = OLD.id;
# # END;
# # """)


# #     connection.commit()
# #     connection.close()

# # # Call this function whenever you want to initialize or reset the database
# # if __name__ == "__main__":
# #     init_db()
# #     print("Database and table initialized successfully.")


# # #create basic functionality 
# # # create ,update the itemquantity

# # # def create_new_item(itemNmae,itemQuantity,price,suplierName,catagory):
# # #     connection= get_db_connection()
# # #     cursor=connection.cursor
# # #     cursor.execute("""
# # # INSER INTO inventory (iteamName,itesmQuantity,price,suplierName,catagory) VALUE(?,?,?,?)
# # # """

# # #     )

# # def create_item(item_name, item_quantity, price, supplier_name, category):
# #     connection = get_db_connection()
# #     cursor = connection.cursor()
# #     cursor.execute("""
# #         INSERT INTO inventory (itemName, itemQuantity, price, supplierName, category)
# #         VALUES (?, ?, ?, ?, ?)
# #     """, (item_name, item_quantity, price, supplier_name, category))
# #     connection.commit()
# #     connection.close()


# # def get_all_items():
# #     connection = get_db_connection()
# #     cursor = connection.cursor()
# #     cursor.execute("SELECT * FROM inventory")
# #     rows = cursor.fetchall()
# #     connection.close()
# #     return [dict(row) for row in rows]  # Convert rows to dictionaries


# # def get_item_by_name(item_name):
# #     connection = get_db_connection()
# #     cursor = connection.cursor()
# #     cursor.execute("SELECT * FROM inventory WHERE itemName = ?", (item_name,))
# #     row = cursor.fetchone()
# #     connection.close()
# #     return dict(row) if row else None
# # def update_item(item_name, item_quantity=None, price=None):
# #     connection = get_db_connection()
# #     cursor = connection.cursor()

# #     # Fetch the current values to use as defaults if none are provided
# #     cursor.execute("SELECT itemQuantity, price FROM inventory WHERE itemName = ?", (item_name,))
# #     row = cursor.fetchone()

# #     if not row:
# #         connection.close()
# #         raise ValueError(f"Item with name '{item_name}' does not exist")

# #     current_quantity, current_price = row

# #     # Use provided values or fallback to existing ones
# #     new_quantity = item_quantity if item_quantity is not None else current_quantity
# #     new_price = price if price is not None else current_price

# #     # Execute the update query
# #     cursor.execute("""
# #         UPDATE inventory
# #         SET itemQuantity = ?, price = ?
# #         WHERE itemName = ?
# #     """, (new_quantity, new_price, item_name))

# #     connection.commit()
# #     connection.close()

# # def delete_item(item_name):
# #     connection = get_db_connection()
# #     cursor = connection.cursor()
# #     cursor.execute("DELETE FROM inventory WHERE itemName = ?", (item_name,))
# #     connection.commit()
# #     connection.close()

# # ## FUNCTION FOR FINANTIAL TRACKING PART
# # def add_transaction(transactionType, amount, category, description, relatedInventoryId):
# #         connection = get_db_connection()
# #         cursor = connection.cursor()
# #         cursor.execute("""
# # INSERT INTO transactions (transactionType, amount, category, description, relatedInventoryId) VALUE (?,?,?,?,?)
# # """,(transactionType, amount, category, description, relatedInventoryId))
# #         cursor.commit()
# #         cursor.close()


# # def get_transactions(filters=None):
# #     connection = get_db_connection()
# #     cursor = connection.cursor()

# #     try:
# #         # Base query
# #         query = "SELECT * FROM transactions"
# #         conditions = []
# #         params = []

# #         # Apply filters dynamically
# #         if filters:
# #             if 'transactionType' in filters:
# #                 conditions.append("transactionType = ?")
# #                 params.append(filters['transactionType'])

# #             if 'category' in filters:
# #                 conditions.append("category = ?")
# #                 params.append(filters['category'])

# #             if 'startDate' in filters and 'endDate' in filters:
# #                 conditions.append("transactionDate BETWEEN ? AND ?")
# #                 params.append(filters['startDate'])
# #                 params.append(filters['endDate'])

# #         # Combine conditions into the query
# #         if conditions:
# #             query += " WHERE " + " AND ".join(conditions)

# #         # Execute the query
# #         cursor.execute(query, params)
# #         transactions = cursor.fetchall()

# #         # Format results into a list of dictionaries
# #         results = [
# #             {
# #                 "id": row[0],
# #                 "transactionType": row[1],
# #                 "amount": row[2],
# #                 "category": row[3],
# #                 "description": row[4],
# #                 "transactionDate": row[5],
# #                 "relatedInventoryId": row[6]
# #             }
# #             for row in transactions
# #         ]

# #     except sqlite3.Error as e:
# #         print(f"An error occurred: {e}")
# #         results = []

# #     finally:
# #         # Close resources
# #         cursor.close()
# #         connection.close()

# #     return results


# # create_item("Laptop", 10, 1500.00, "Tech Supplier", "Electronics")
# # create_item("Headphones", 50, 200.00, "AudioWorld", "Accessories")

# # # Test getting all items
# # items = get_all_items()
# # print("All Items:", items)

# # # Test getting a specific item by name
# # item = get_item_by_name("Laptop")
# # print("Laptop Details:", item)

# # # Test updating an item
# # update_item("Laptop", item_quantity=15)  # Update quantity only
# # updated_item = get_item_by_name("Laptop")
# # print("Updated Laptop:", updated_item)

# # # Test deleting an item
# # delete_item("Headphones")
# # items_after_deletion = get_all_items()
# # print("Items After Deletion:", items_after_deletion)



# import sqlite3
# import os

# def get_db_connection():
#     db_path = os.path.join(os.path.dirname(__file__), 'app.db')
#     connection = sqlite3.connect(db_path)
#     connection.row_factory = sqlite3.Row
#     return connection

# def init_db():
#     try:
#         connection = get_db_connection()
#         cursor = connection.cursor()
#         cursor.executescript("""
#         CREATE TABLE IF NOT EXISTS inventory (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             itemName TEXT NOT NULL,
#             itemQuantity INT NOT NULL DEFAULT 0 CHECK (itemQuantity >= 0),
#             price DECIMAL(10, 2) NOT NULL DEFAULT 0.00 CHECK (price >= 0),
#             createdTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#             updatedTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#             stockStatus TEXT DEFAULT 'In Stock' CHECK (stockStatus IN ('In Stock', 'Out of Stock')),
#             supplierName TEXT,
#             category TEXT NOT NULL DEFAULT 'Uncategorized'
#         );

#         CREATE TRIGGER IF NOT EXISTS update_updatedTime
#         AFTER UPDATE ON inventory
#         FOR EACH ROW
#         BEGIN
#             UPDATE inventory SET updatedTime = CURRENT_TIMESTAMP WHERE id = OLD.id;
#         END;

#         CREATE TABLE IF NOT EXISTS transactions (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             transactionType TEXT CHECK(transactionType IN ('Income', 'Expense')) NOT NULL,
#             amount REAL NOT NULL CHECK(amount >=0),
#             category TEXT NOT NULL,
#             description TEXT,
#             transactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
#             updatedTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#             relatedInventoryId INTEGER,
#             FOREIGN KEY (relatedInventoryId) REFERENCES inventory(id)
#         );

#         CREATE TRIGGER IF NOT EXISTS update_updatedTime
#         AFTER UPDATE ON transactions
#         FOR EACH ROW
#         BEGIN
#             UPDATE transactions SET updatedTime = CURRENT_TIMESTAMP WHERE id = OLD.id;
#         END;
#         """)
#         connection.commit()
#     except sqlite3.Error as e:
#         print(f"An error occurred during database initialization: {e}")
#     finally:
#         connection.close()

# def create_item(item_name, item_quantity, price, supplier_name, category):
#     try:
#         connection = get_db_connection()
#         cursor = connection.cursor()
#         cursor.execute("""
#             INSERT INTO inventory (itemName, itemQuantity, price, supplierName, category)
#             VALUES (?, ?, ?, ?, ?)
#         """, (item_name, item_quantity, price, supplier_name, category))
#         connection.commit()
#     except sqlite3.Error as e:
#         print(f"An error occurred while creating an item: {e}")
#     finally:
#         connection.close()

# def get_all_items():
#     try:
#         connection = get_db_connection()
#         cursor = connection.cursor()
#         cursor.execute("SELECT * FROM inventory")
#         rows = cursor.fetchall()
#         return [dict(row) for row in rows]
#     except sqlite3.Error as e:
#         print(f"An error occurred while fetching all items: {e}")
#         return []
#     finally:
#         connection.close()

# def get_item_by_name(item_name):
#     try:
#         connection = get_db_connection()
#         cursor = connection.cursor()
#         cursor.execute("SELECT * FROM inventory WHERE itemName = ?", (item_name,))
#         row = cursor.fetchone()
#         return dict(row) if row else None
#     except sqlite3.Error as e:
#         print(f"An error occurred while fetching item by name: {e}")
#         return None
#     finally:
#         connection.close()

# def update_item(item_name, item_quantity=None, price=None):
#     try:
#         connection = get_db_connection()
#         cursor = connection.cursor()
#         cursor.execute("SELECT itemQuantity, price FROM inventory WHERE itemName = ?", (item_name,))
#         row = cursor.fetchone()

#         if not row:
#             raise ValueError(f"Item with name '{item_name}' does not exist")

#         current_quantity, current_price = row
#         new_quantity = item_quantity if item_quantity is not None else current_quantity
#         new_price = price if price is not None else current_price

#         cursor.execute("""
#             UPDATE inventory
#             SET itemQuantity = ?, price = ?
#             WHERE itemName = ?
#         """, (new_quantity, new_price, item_name))
#         connection.commit()
#     except (sqlite3.Error, ValueError) as e:
#         print(f"An error occurred while updating item: {e}")
#     finally:
#         connection.close()

# def delete_item(item_name):
#     try:
#         connection = get_db_connection()
#         cursor = connection.cursor()
#         cursor.execute("DELETE FROM inventory WHERE itemName = ?", (item_name,))
#         connection.commit()
#     except sqlite3.Error as e:
#         print(f"An error occurred while deleting item: {e}")
#     finally:
#         connection.close()

# def add_transaction(transactionType, amount, category, description, relatedInventoryId):
#     try:
#         connection = get_db_connection()
#         cursor = connection.cursor()
#         cursor.execute("""
#             INSERT INTO transactions (transactionType, amount, category, description, relatedInventoryId)
#             VALUES (?, ?, ?, ?, ?)
#         """, (transactionType, amount, category, description, relatedInventoryId))
#         connection.commit()
#     except sqlite3.Error as e:
#         print(f"An error occurred while adding a transaction: {e}")
#     finally:
#         connection.close()

# def get_transactions(filters=None):
#     try:
#         connection = get_db_connection()
#         cursor = connection.cursor()
#         query = "SELECT * FROM transactions"
#         conditions = []
#         params = []

#         if filters:
#             if 'transactionType' in filters:
#                 conditions.append("transactionType = ?")
#                 params.append(filters['transactionType'])

#             if 'category' in filters:
#                 conditions.append("category = ?")
#                 params.append(filters['category'])

#             if 'startDate' in filters and 'endDate' in filters:
#                 conditions.append("transactionDate BETWEEN ? AND ?")
#                 params.append(filters['startDate'])
#                 params.append(filters['endDate'])

#         if conditions:
#             query += " WHERE " + " AND ".join(conditions)

#         cursor.execute(query, params)
#         transactions = cursor.fetchall()

#         return [
#             {
#                 "id": row[0],
#                 "transactionType": row[1],
#                 "amount": row[2],
#                 "category": row[3],
#                 "description": row[4],
#                 "transactionDate": row[5],
#                 "relatedInventoryId": row[6]
#             }
#             for row in transactions
#         ]
#     except sqlite3.Error as e:
#         print(f"An error occurred while fetching transactions: {e}")
#         return []
#     finally:
#         connection.close()


# def delete_transaction(transactionId):
#     try:
#         connection = get_db_connection()
#         cursor = connection.cursor()

#         # Check if the transaction exists
#         cursor.execute("SELECT * FROM transactions WHERE id = ?", (transactionId,))
#         transaction = cursor.fetchone()
#         if not transaction:
#             raise ValueError(f"Transaction with ID {transactionId} does not exist.")

#         # Perform the deletion
#         cursor.execute("DELETE FROM transactions WHERE id = ?", (transactionId,))

#         # Commit the changes
#         connection.commit()
#         print(f"Transaction with ID {transactionId} has been successfully deleted.")

#     except ValueError as ve:
#         print(f"Validation Error: {ve}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#     finally:
#         # Ensure resources are closed
#         cursor.close()
#         connection.close()

# if __name__ == "__main__":
#     init_db()
#     print("Database and table initialized successfully.")

#     create_item("Laptop", 10, 1500.00, "Tech Supplier", "Electronics")
#     create_item("Headphones", 50, 200.00, "AudioWorld", "Accessories")

#     items = get_all_items()
#     print("All Items:", items)

#     item = get_item_by_name("Laptop")
#     print("Laptop Details:", item)

#     update_item("Laptop", item_quantity=15)
#     updated_item = get_item_by_name("Laptop")
#     print("Updated Laptop:", updated_item)

#     delete_item("Headphones")
#     items_after_deletion = get_all_items()
#     print("Items After Deletion:", items_after_deletion)


import sqlite3
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_db_connection():
    db_path = os.path.join(os.path.dirname(__file__), 'app.db')
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    return connection

def init_db():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
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

        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            transactionType TEXT CHECK(transactionType IN ('Income', 'Expense')) NOT NULL,
            amount REAL NOT NULL CHECK(amount >=0),
            category TEXT NOT NULL,
            description TEXT,
            transactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            updatedTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            relatedInventoryId INTEGER,
            FOREIGN KEY (relatedInventoryId) REFERENCES inventory(id)
        );

        CREATE TRIGGER IF NOT EXISTS update_updatedTime
        AFTER UPDATE ON transactions
        FOR EACH ROW
        BEGIN
            UPDATE transactions SET updatedTime = CURRENT_TIMESTAMP WHERE id = OLD.id;
        END;
        """)
        connection.commit()
        logging.info("Database and tables initialized successfully.")
    except sqlite3.Error as e:
        logging.error(f"An error occurred during database initialization: {e}")
    finally:
        connection.close()

def create_item(item_name, item_quantity, price, supplier_name, category):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO inventory (itemName, itemQuantity, price, supplierName, category)
            VALUES (?, ?, ?, ?, ?)
        """, (item_name, item_quantity, price, supplier_name, category))
        connection.commit()
        logging.info(f"Item '{item_name}' created successfully.")
    except sqlite3.Error as e:
        logging.error(f"An error occurred while creating an item: {e}")
    finally:
        connection.close()

def get_all_items():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM inventory")
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    except sqlite3.Error as e:
        logging.error(f"An error occurred while fetching all items: {e}")
        return []
    finally:
        connection.close()

def get_item_by_name(item_name):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM inventory WHERE itemName = ?", (item_name,))
        row = cursor.fetchone()
        return dict(row) if row else None
    except sqlite3.Error as e:
        logging.error(f"An error occurred while fetching item by name: {e}")
        return None
    finally:
        connection.close()

def update_item(item_name, item_quantity=None, price=None):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT itemQuantity, price FROM inventory WHERE itemName = ?", (item_name,))
        row = cursor.fetchone()

        if not row:
            raise ValueError(f"Item with name '{item_name}' does not exist")

        current_quantity, current_price = row
        new_quantity = item_quantity if item_quantity is not None else current_quantity
        new_price = price if price is not None else current_price

        cursor.execute("""
            UPDATE inventory
            SET itemQuantity = ?, price = ?
            WHERE itemName = ?
        """, (new_quantity, new_price, item_name))
        connection.commit()
        logging.info(f"Item '{item_name}' updated successfully.")
    except (sqlite3.Error, ValueError) as e:
        logging.error(f"An error occurred while updating item: {e}")
    finally:
        connection.close()

def delete_item(item_name):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM inventory WHERE itemName = ?", (item_name,))
        connection.commit()
        logging.info(f"Item '{item_name}' deleted successfully.")
    except sqlite3.Error as e:
        logging.error(f"An error occurred while deleting item: {e}")
    finally:
        connection.close()

def add_transaction(transactionType, amount, category, description, relatedInventoryId):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO transactions (transactionType, amount, category, description, relatedInventoryId)
            VALUES (?, ?, ?, ?, ?)
        """, (transactionType, amount, category, description, relatedInventoryId))
        connection.commit()
        logging.info("Transaction added successfully.")
    except sqlite3.Error as e:
        logging.error(f"An error occurred while adding a transaction: {e}")
    finally:
        connection.close()
def get_transactions(filters=None):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM transactions"
        conditions = []
        params = []

        if filters!=None:
            if 'transactionType' in filters:
                conditions.append("transactionType = ?")
                params.append(filters['transactionType'])

            if 'category' in filters:
                conditions.append("category = ?")
                params.append(filters['category'])

            if 'startDate' in filters and 'endDate' in filters:
                conditions.append("transactionDate BETWEEN ? AND ?")
                params.append(filters['startDate'])
                params.append(filters['endDate'])
        else:
            cursor.execute("SELECT * FROM inventory")
            rows = cursor.fetchall()
            return [dict(row) for row in rows]

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        # Debugging: Print the query and parameters
        print(f"Executing query: {query}")
        print(f"With parameters: {params}")

        cursor.execute(query, params)
        transactions = cursor.fetchall()

        return [
            {
                "id": row[0],
                "transactionType": row[1],
                "amount": row[2],
                "category": row[3],
                "description": row[4],
                "transactionDate": row[5],
                "relatedInventoryId": row[6]
            }
            for row in transactions
        ]
    except sqlite3.Error as e:
        logging.error(f"An error occurred while fetching transactions: {e}")
        return []
    finally:
        connection.close()
# def get_transactions(filters=None):
#     try:
#         connection = get_db_connection()
#         cursor = connection.cursor()
#         query = "SELECT * FROM transactions"
#         conditions = []
#         params = []

#         if filters:
#             if 'transactionType' in filters:
#                 conditions.append("transactionType = ?")
#                 params.append(filters['transactionType'])

#             if 'category' in filters:
#                 conditions.append("category = ?")
#                 params.append(filters['category'])

#             if 'startDate' in filters and 'endDate' in filters:
#                 conditions.append("transactionDate BETWEEN ? AND ?")
#                 params.append(filters['startDate'])
#                 params.append(filters['endDate'])

#         if conditions:
#             query += " WHERE " + " AND ".join(conditions)

#         cursor.execute(query, params)
#         transactions = cursor.fetchall()

#         return [
#             {
#                 "id": row[0],
#                 "transactionType": row[1],
#                 "amount": row[2],
#                 "category": row[3],
#                 "description": row[4],
#                 "transactionDate": row[5],
#                 "relatedInventoryId": row[6]
#             }
#             for row in transactions
#         ]
#     except sqlite3.Error as e:
#         logging.error(f"An error occurred while fetching transactions: {e}")
#         return []
#     finally:
#         connection.close()

def delete_transaction(transactionId):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Check if the transaction exists
        cursor.execute("SELECT * FROM transactions WHERE id = ?", (transactionId,))
        transaction = cursor.fetchone()
        if not transaction:
            raise ValueError(f"Transaction with ID {transactionId} does not exist.")

        # Perform the deletion
        cursor.execute("DELETE FROM transactions WHERE id = ?", (transactionId,))
        connection.commit()
        logging.info(f"Transaction with ID {transactionId} has been successfully deleted.")
    except ValueError as ve:
        logging.error(f"Validation Error: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    init_db()

    create_item("Laptop", 10, 1500.00, "Tech Supplier", "Electronics")
    create_item("Headphones", 50, 200.00, "AudioWorld", "Accessories")

    items = get_all_items()
    logging.info(f"All Items: {items}")

    item = get_item_by_name("Laptop")
    logging.info(f"Laptop Details: {item}")

    update_item("Laptop", item_quantity=15)
    updated_item = get_item_by_name("Laptop")
    logging.info(f"Updated Laptop: {updated_item}")

    delete_item("Headphones")
    items_after_deletion = get_all_items()
    logging.info(f"Items After Deletion: {items_after_deletion}")