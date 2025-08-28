## Put and delete HTTPS verbs
## working with APIs

from flask import Flask, request, jsonify

# Create a Flask application
app = Flask(__name__)

# Sample data
items = [{'id':1, 'name':'Item 1', 'description':'This is Item 1'},
         {'id':2, 'name':'Item 2', 'description':'This is Item 2'},
         {'id':3, 'name':'Item 3', 'description':'This is Item 3'}]

@app.route('/')
def home():
    return 'Welcome to the sample data to TO-DO List App'

# Get retrieve all the data
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# get: 

if __name__ == "__main__":
    app.run(debug=True)