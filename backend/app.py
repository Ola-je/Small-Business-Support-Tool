
from flask import Flask

from routes.inventory_routes import inventory_routes
from routes.exchange_routes import exchange_bp
from routes.inventory_analytics import analytics_bp


app = Flask(__name__)
app.register_blueprint(inventory_routes)
app.register_blueprint(exchange_bp)
app.register_blueprint(analytics_bp)



@app.route('/')
def home():
    return "Welcome to the Small Business Support Tool!"

if __name__ == '__main__':
    app.run(debug=True)