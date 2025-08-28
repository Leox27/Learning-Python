from flask import Flask, render_template

# Create a Flask application
app = Flask(__name__)

# Route for the main webpage
@app.route("/")

def webpage():
    
    # return "Welcome to my portfolio you visitors"
    return "Welcome to my Portfolio"

# Route for the index page
@app.route("/index")

def index():
    return "index section"

if __name__ == "__main__":

    app.run(debug=True)
