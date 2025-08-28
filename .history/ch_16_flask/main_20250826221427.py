from flask import Flask

app = Flask(__name__)

# 
@app.route("/")
def webpage():
    return "Welcome to my Portfolio"

@app.route("/index")
def index():
    return "Index page"

if __name__ == "__main__":

    app.run()
