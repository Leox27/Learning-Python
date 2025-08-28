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
    return render_template("", result)


@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':

        # Handle form submission
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Process the data (e.g., save to database, send email, etc.)
        return f"""
        <h1>Thank you, {name}!</h1>
        <p>We received your message:</p>
        <blockquote>{message}</blockquote>
        <p>We will reach out to you at <b>{email}</b>.</p>
        <p><a href='/form'>⬅ Back to Form</a></p>
    """
    return render_template('form.html')

if __name__ == "__main__":

    app.run(debug=True)
