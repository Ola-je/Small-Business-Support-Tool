# Small-Business-Support-Tool
A Python-based web application that helps small business owners manage inventory, track finances, and integrate real-time currency exchange. Supports economic growth by enhancing productivity and job creation.


# Flask Inventory Management API Documentation

This API provides CRUD operations (Create, Read, Update, Delete) for managing an inventory system. Here's everything your team needs to set up the environment and understand how the system works.

---

## Environment Setup

1. **Python Version**: 
   - Use Python 3.10+ to ensure compatibility with Flask and SQLite.

2. **Virtual Environment**:
   - Create a virtual environment for isolating project dependencies.
   - Commands for creating and activating the environment:
     - **Windows**: `venv\Scripts\activate`
     - **Mac/Linux**: `source venv/bin/activate`

3. **Dependencies**:
   - Install Flask: `pip install flask`
   - If cross-origin requests are needed in the future (e.g., frontend integration), install Flask-CORS: `pip install flask-cors`.

4. **Running the Application**:
   - Once the environment is set up, run the app with `python app.py`.
   - The server will be accessible at `http://127.0.0.1:5000`.

---

## Database Design and Structure

1. **Database**:
   - The project uses SQLite (`app.db`) stored in the `db/` folder.
   - The database is automatically created and initialized with the required table when the app runs for the first time.

2. **Inventory Table**:
   - The table `inventory` has the following columns:
     - **id**: Auto-incremented unique identifier.
     - **itemName**: Name of the inventory item.
     - **itemQuantity**: Quantity available (default is 0).
     - **price**: Price per item.
     - **supplierName**: Optional, the supplier's name.
     - **category**: Optional, the category of the item.
     - **createdTime**: Timestamp of item creation.
     - **updatedTime**: Automatically updated timestamp for modifications.

3. **Auto-Update Trigger**:
   - A trigger updates the `updatedTime` whenever an item is modified.

---

## Routes Overview

1. **Route List**:
   - **POST `/create-item`**: Adds a new item to the inventory. Requires a JSON payload with item details.
   - **GET `/items`**: Retrieves a list of all items in the inventory.
   - **GET `/item/<itemName>`**: Fetches details of a specific item using its name.
   - **PUT `/update-item/<itemName>`**: Updates details of an existing item. Accepts partial updates through a JSON payload.
   - **DELETE `/delete-item/<itemName>`**: Deletes an item from the inventory by its name.

2. **Route Behavior**:
   - Each route interacts with `database.py` to perform database operations.
   - Routes act as the interface between the client (Postman, curl, etc.) and the database.

---

## How It Works

1. **Routes**:
   - Routes are defined in `inventory_routes.py` and use Flask's `Blueprint` for modularity.
   - They validate incoming requests (e.g., JSON payloads) and handle HTTP methods (POST, GET, PUT, DELETE).

2. **Database Functions**:
   - All database logic is defined in `database.py` to keep the code modular and reusable.
   - Functions include: creating, fetching, updating, and deleting items.

3. **Process**:
   - The client sends an HTTP request (e.g., POST, GET).
   - The corresponding route processes the request and calls a database function from `database.py`.
   - The response (success or error) is returned to the client in JSON format.

---

## Testing

1. **Testing Tools**:
   - Use **Postman** or `curl` to send HTTP requests to the server.
   - Ensure the app is running locally (`http://127.0.0.1:5000`) before testing.

2. **Testing Steps**:
   - Send requests to endpoints with the correct HTTP methods and payloads.
   - Check responses for success messages or data validation errors.

3. **Sample Test Scenarios**:
   - **Create Item**: Send a POST request to `/create-item` with item details in the JSON body.
   - **Retrieve Items**: Send a GET request to `/items` or `/item/<itemName>`.
   - **Update Item**: Send a PUT request to `/update-item/<itemName>` with updated fields in the JSON body.
   - **Delete Item**: Send a DELETE request to `/delete-item/<itemName>`.

---


