from flask import Flask,render_template
from jinja2 import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/overview')
def overview():
    return render_template('overview.html')

@app.route('/reports')
def register():
   return render_template('reports.html')

@app.route('/machine')
def dashboard():
    return render_template('machine.html')

if __name__ == "__main__":
   app.run(debug=True)
