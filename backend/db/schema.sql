-- CREATE TABLE IF NOT EXISTS inventory(
--     id INT PRIYMARY KEY AOUTOINCREAMENT,
--     itemName TEXT NOT NULL UNIQUE,
--     itemQuantity INT NOT NULL CHECK(itemQuantity=>0),
--     price INT Not null,
--     categories TEXT NOT NULL,
--     createdTime TIMESTAMP 
--     updatedTime TIMESTAMP ON UPDATE TIMESTAMP
--     stockstatuss VARCHAR(10) CHECK(itemQuantity IN('IN STOCK,OUT STOCK'))

-- )
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

