from flask import Flask, render_template, request, redirect, url_for

# Setup Flask and login
app = Flask(__name__)

# INDEX
@app.route('/')
@app.route('/index')
def gameplay():
    """Show the game play page."""
    return render_template('game.html')

@app.route('/inventory')
def inventory():
    """Show all items via the inventory page."""
    return render_template('inventory.html')

