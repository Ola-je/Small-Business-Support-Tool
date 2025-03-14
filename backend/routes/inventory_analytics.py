from flask import Blueprint, jsonify
from db.database import get_db_connection

# Create a Blueprint for analytics endpoints
analytics_bp = Blueprint('inventory_analytics', __name__)

# Define the low-stock threshold
LOW_STOCK_THRESHOLD = 5

def check_low_stock_alerts():
    """
    Query the database for items with a quantity below the LOW_STOCK_THRESHOLD.
    Returns a list of dictionaries for low-stock items.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT itemName, itemQuantity FROM inventory WHERE itemQuantity < ?", (LOW_STOCK_THRESHOLD,))
    low_stock_items = cursor.fetchall()
    connection.close()
    return [dict(item) for item in low_stock_items]

def get_inventory_value():
    """
    Calculates the total inventory value as the sum of (price * itemQuantity) for all items.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT SUM(price * itemQuantity) AS total_value FROM inventory")
    row = cursor.fetchone()
    connection.close()
    return row["total_value"] if row["total_value"] is not None else 0

def get_total_items():
    """
    Returns the total count of inventory items.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) AS total_items FROM inventory")
    row = cursor.fetchone()
    connection.close()
    return row["total_items"]

# Endpoint: Get low-stock alerts
@analytics_bp.route('/low-stock-alerts', methods=['GET'])
def low_stock_alerts():
    """
    API endpoint that returns a list of items with low stock.
    """
    items = check_low_stock_alerts()
    if not items:
        return jsonify({"message": "All items are sufficiently stocked."}), 200
    return jsonify({"low_stock_items": items}), 200

# Endpoint: Get financial summary
@analytics_bp.route('/financial-summary', methods=['GET'])
def financial_summary():
    """
    API endpoint that returns the total inventory value and the total number of items.
    """
    total_value = get_inventory_value()
    total_items = get_total_items()
    return jsonify({
        "total_inventory_value": round(total_value, 2),
        "total_items": total_items
    }), 200
