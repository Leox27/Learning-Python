from flask import Flask

app = Flask(__name__)

@app.route("/")

def webpage():
    return "Welcome to the my Portfilio"

if __name__ == "__main__":

    app.run()
