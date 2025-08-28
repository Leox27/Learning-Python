from flask import Flask, render_template

# Create a Flask application
app = Flask(__name__)

# Route for the main webpage
@app.route("/")

def webpage():
    
    # return "Welcome to my portfolio you visitors"
    return f"<html><h1>Welcome to my Portfolio - Last updated</h1></body></html>"
# Route for the index page
@app.route("/index")

def index():
    return "<html><h1>Index page</h1></body></html>"


if __name__ == "__main__":

    app.run(debug=True)
