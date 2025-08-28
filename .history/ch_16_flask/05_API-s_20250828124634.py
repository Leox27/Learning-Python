## Put and delete HTTPS verbs
## working with APIs

from flask import Flask, request, jsonify

# Create a Flask application
app = Flask(__name__)
items = [{'id':1, 'name':'Item 1', 'description':'This is Item 1'},
         {'id':2, 'name':'Item 2', 'description':'This is Item 2'},
         {'id':3, 'name':'Item 3', 'description':'This is Item 3'}]