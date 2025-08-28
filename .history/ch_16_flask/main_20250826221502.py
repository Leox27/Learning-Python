from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Route for the main webpage
@app.route("/")
def webpage():
    return "Welcome to my Portfolio"

# Route for the index page
@app.route("/index")
def index():
    return "Index page"

# 
if __name__ == "__main__":

    app.run()
