from flask import Flask, render_template, request, redirect, url_for

# Setup Flask and login
app = Flask(__name__)

# INDEX
@app.route('/')
@app.route('/index')
def items_index():
    """Show all items via the Home page which is accessible to anyone."""
    #return render_template('visitor.html')
    return render_template('index.html')
