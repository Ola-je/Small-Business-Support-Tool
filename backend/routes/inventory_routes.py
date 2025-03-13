from flask import Blueprint, request, jsonify
from db.database import create_item, get_all_items, get_item_by_name, update_item, delete_item

# Create a Blueprint for inventory routes
inventory_routes = Blueprint('inventory_routes', __name__)

# Route to create a new item
@inventory_routes.route('/create-item', methods=['POST'])
def create_inventory_item():
    data = request.json  # Get JSON payload from the request
    create_item(
        data['itemName'], 
        data['itemQuantity'], 
        data['price'], 
        data.get('supplierName', ''),  # Optional, defaults to an empty string
        data.get('category', 'Uncategorized')  # Optional, defaults to 'Uncategorized'
    )
    return jsonify({"message": f"Item '{data['itemName']}' created successfully."}), 201

# Route to get all items
@inventory_routes.route('/items', methods=['GET'])
def get_inventory_items():
    items = get_all_items()
    return jsonify(items), 200  # Return the items as JSON with status 200

# Route to get a specific item by its name
@inventory_routes.route('/item/<string:item_name>', methods=['GET'])
def get_inventory_item(item_name):
    item = get_item_by_name(item_name)
    if item:
        return jsonify(item), 200
    return jsonify({"error": f"Item '{item_name}' not found."}), 404

# Route to update an item
@inventory_routes.route('/update-item/<string:item_name>', methods=['PUT'])
def update_inventory_item(item_name):
    data = request.json  # Get JSON payload from the request
    try:
        update_item(
            item_name,
            item_quantity=data.get('itemQuantity'),  # None if not provided
            price=data.get('price')  # None if not provided
        )
        return jsonify({"message": f"Item '{item_name}' updated successfully."}), 200
    except ValueError as e:  # Handle cases where the item does not exist
        return jsonify({"error": str(e)}), 404

# Route to delete an item by its name
@inventory_routes.route('/delete-item/<string:item_name>', methods=['DELETE'])
def delete_inventory_item(item_name):
    delete_item(item_name)
    return jsonify({"message": f"Item '{item_name}' deleted successfully."}), 200
