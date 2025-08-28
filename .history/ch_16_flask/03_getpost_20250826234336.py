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

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Process the data (e.g., save to database, send email, etc.)
        return f"Thank you {name}, your message has been received!"
    return render_template('form.html')

if __name__ == "__main__":

    app.run(debug=True)
