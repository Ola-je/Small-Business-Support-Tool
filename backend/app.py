
from flask import Flask

from routes.inventory_routes import inventory_routes
from routes.financial_routes import financial_blueprint

app = Flask(__name__)
app.register_blueprint(inventory_routes)
app.register_blueprint(financial_blueprint)

@app.route('/')
def home():
    return "Welcome to the Small Business Support Tool!"

if __name__ == '__main__':
    app.run(debug=True)