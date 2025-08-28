from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Route for the main webpage
@app.route("/")

def webpage():
    from datetime import datetime
    # return "Welcome to my portfolio you visitors"
    return f"<html><body>Welcome to my Portfolio - Last updated: {datetime.now().strftime('%H:%M:%S')}</body></html>"
# Route for the index page
@app.route("/index")

def index():
    return "Index page hii"


if __name__ == "__main__":

    app.run(debug=True)
