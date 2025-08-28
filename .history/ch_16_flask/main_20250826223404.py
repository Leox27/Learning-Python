from flask import Flask
from datetime import datetime

# Create a Flask application
app = Flask(__name__)

# Route for the main webpage
@app.route("/")
def webpage():
    return f"Welcome to my Portfolio - Last updated: {datetime.now().strftime('%H:%M:%S')}"

# Route for the index page
@app.route("/index")
def index():
    return "Index page hii"

if __name__ == "__main__":
    app.run(debug=True, port=5000, use_reloader=True)
