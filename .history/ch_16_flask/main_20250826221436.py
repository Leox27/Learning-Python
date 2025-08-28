from flask import Flask

app = Flask(__name__)

# Route for the main webpage
@app.route("/")
def webpage():
    return "Welcome to my Portfolio"

# 
@app.route("/index")
def index():
    return "Index page"

if __name__ == "__main__":

    app.run()
