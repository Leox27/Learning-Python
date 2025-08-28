from flask import Flask

app = Flask(__name__)

@app.route("/")
def webpage():
    return """Welcome to the my Portfolio
    My name is Mayur Jadha"""

@app.route("/index")
def index():
    return "Index page"

if __name__ == "__main__":

    app.run(debug=True)
