from flask import Blueprint, request, jsonify
from database import add_transaction, get_transactions, update_transaction, delete_transaction

# Define the Blueprint
financial_blueprint = Blueprint("financial", __name__)

# 1. POST /add-transaction
@financial_blueprint.route("/add-transaction", methods=["POST"])
def add_transaction_route():
    try:
        data = request.get_json()
        add_transaction(
            transactionType=data["transactionType"],
            amount=data["amount"],
            category=data["category"],
            description=data.get("description"),
            relatedInventoryId=data.get("relatedInventoryId"),
        )
        return jsonify({"message": "Transaction added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# 2. GET /transactions
@financial_blueprint.route("/transactions", methods=["GET"])
def get_transactions_route():
    try:
        filters = {
            "transactionType": request.args.get("transactionType"),
            "category": request.args.get("category"),
            "startDate": request.args.get("startDate"),
            "endDate": request.args.get("endDate"),
        }
        transactions = get_transactions(filters)
        return jsonify(transactions), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# 3. PUT /update-transaction/<transactionId>
@financial_blueprint.route("/update-transaction/<int:transactionId>", methods=["PUT"])
def update_transaction_route(transactionId):
    try:
        data = request.get_json()
        update_transaction(
            transactionId=transactionId,
            transactionType=data.get("transactionType"),
            amount=data.get("amount"),
            category=data.get("category"),
            description=data.get("description"),
            transactionDate=data.get("transactionDate"),
            relatedInventoryId=data.get("relatedInventoryId"),
        )
        return jsonify({"message": f"Transaction ID {transactionId} updated successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# 4. DELETE /delete-transaction/<transactionId>
@financial_blueprint.route("/delete-transaction/<int:transactionId>", methods=['DELETE'])
def delete_transaction_route(transactionId):
    try:
        data=request.get_json
        delete_transaction(transactionId=data.get["transactionid"])
        return jsonify({"message":f"Transaction ID {transactionId} deleted successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    