## Put and delete HTTPS verbs
## working with APIs

from flask import Flask, request, jsonify

# Create a Flask application
app = Flask(__name__)

# Sample data
items = [{'id':1, 'name':'Item 1', 'description':'This is Item 1'},
         {'id':2, 'name':'Item 2', 'description':'This is Item 2'},
         {'id':3, 'name':'Item 3', 'description':'This is Item 3'}]

# Home route
@app.route('/')

def home():
    return 'Welcome to the sample data to TO-DO List App'

# Get retrieve all the data
@app.route('/items', methods=['GET'])

def get_items():
    return jsonify(items)

# Get a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])

def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    return jsonify(item) if item else ('', 404)

# Create a new item
@app.route('/itemsj', methods=['POST'])

def create_item():
    
    return if not request.jsonify(new_item), 201
    new_name = { "name": new_item["name"], "description": new_item["description"] }
    return jsonify(new_name), 201



if __name__ == "__main__":
    app.run(debug=True)