from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Route for the main webpage
@app.route("/")

def webpage():
    
    # return "Welcome to my portfolio you visitors"
    return f"<html><body>Welcome to my Portfolio - Last updated</body></html>"
# Route for the index page
@app.route("/index")

def index():
    return "<html><body>Index page hii</body></html>"


if __name__ == "__main__":

    app.run(debug=True)
