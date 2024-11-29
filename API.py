from flask import Flask, request, jsonify

app = Flask(_name_)

# In-memory product list to store products
products = []

# Product class to represent the product fields
class Product:
    def _init_(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

# POST /products: Accepts a JSON object to create a new product
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    if not data or 'name' not in data or 'description' not in data or 'price' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    try:
        # Create a new product and add to the products list
        product = Product(data['name'], data['description'], float(data['price']))
        products.append(product)
        return jsonify({'message': 'Product created successfully'}), 201
    except ValueError:
        return jsonify({'error': 'Invalid price format'}), 400

# GET /products: Retrieves a list of all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify([{
        'name': product.name,
        'description': product.description,
        'price': product.price
    } for product in products]), 200

if _name_ == '_main_':
    app.run(debug=True)