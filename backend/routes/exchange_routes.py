from flask import Blueprint, request, jsonify
from currency_exchange.exchange import convert_currency

exchange_bp = Blueprint('exchange', __name__)

@exchange_bp.route('/exchange', methods=['GET'])
def exchange():
    """
    API endpoint for currency conversion.
    Example: /exchange?amount=100&from=USD&to=EUR
    """
    try:
        base_currency = request.args.get('from', 'USD').upper()
        target_currency = request.args.get('to', 'EUR').upper()
        amount = float(request.args.get('amount', 1))
        
        converted_amount = convert_currency(amount, base_currency, target_currency)
        
        if converted_amount is not None:
            return jsonify({
                "base_currency": base_currency,
                "target_currency": target_currency,
                "original_amount": amount,
                "converted_amount": converted_amount
            })
        return jsonify({"error": "Conversion failed."}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 400
