
from flask import Flask

from routes.inventory_routes import inventory_routes

app = Flask(__name__)
app.register_blueprint(inventory_routes)

@app.route('/')
def home():
    return "Welcome to the Small Business Support Tool!"

if __name__ == '__main__':
    app.run(debug=True)