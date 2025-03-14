import requests
from currency_exchange.config import OPEN_EXCHANGE_API_KEY, BASE_URL

def get_exchange_rate(base_currency, target_currency):
    """
    Fetch real-time exchange rate from Open Exchange Rates API.
    """
    try:
        response = requests.get(f"{BASE_URL}?app_id={OPEN_EXCHANGE_API_KEY}")
        data = response.json()
        
        if "rates" in data:
            rates = data["rates"]
            if base_currency in rates and target_currency in rates:
                return rates[target_currency] / rates[base_currency]
            else:
                raise ValueError("Invalid currency code.")
        else:
            raise Exception("Failed to fetch exchange rates.")
    
    except Exception as e:
        print("Error fetching exchange rate:", e)
        return None

def convert_currency(amount, base_currency, target_currency):
    """
    Convert amount from base_currency to target_currency.
    """
    rate = get_exchange_rate(base_currency, target_currency)
    return round(amount * rate, 2) if rate else None
