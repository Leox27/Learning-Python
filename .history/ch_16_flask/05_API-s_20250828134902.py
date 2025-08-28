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

# POSTCreate a new item
@app.route('/items', methods=['POST'])

def create_item():
    if not request.json or not 'name' in request.json:
        return ('', 400)
    new_item = {
        "id": len(items) + 1,
        "name": request.json["name"],
        "description": request.json.get("description", "")
    }
    items.append(new_item)
    return jsonify(new_item), 201

if __name__ == "__main__":
    app.run(debug=True)