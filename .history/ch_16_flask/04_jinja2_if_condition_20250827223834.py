### Building URL dynamically
### Variable Rules
### jinja templating


## jinja 2 templates
'''
{{ }} expression for jinja 2 template
{%...%} used for- loops
{#...#} used for comments
'''

from flask import Flask, render_template, request

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
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

# variable rule 
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"
    return render_template("result.html", results = res)

# variable rule 
@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score >= 35:
        res = "PASSED"
    else:
        res = "FAILED"
    
    exp = {'score':score, 'result':res}
    return render_template('result1.html', results = exp)

# 

if __name__ == "__main__":

    app.run(debug=True)
