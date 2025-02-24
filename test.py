from flask import Flask,render_template, send_file
from jinja2 import *
import pandas as pd
import io
from xlsxwriter import Workbook

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/over')
def over():
    return render_template('overview.html')

@app.route('/reports')
def register():
   return render_template('reports.html')

@app.route('/machine')
def dashboard():
    return render_template('machine.html')
@app.route('/pareto')
def pareto():
    return render_template('pareto.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/support')
def support():
    return render_template('support.html')


@app.route('/download_excel')
def download_excel():
    # Define data (matching the chart data)
    data = {
        "Category": ["Die Changed planned", "Power Fluctuation", "Mechanical"],
        "Downtime (Minutes)": [3, 15, 15]
    }

    # Convert to Pandas DataFrame
    df = pd.DataFrame(data)

    # Save to an in-memory Excel file
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Downtime Data")
    
    output.seek(0)

    # Serve the file for download
    return send_file(output, as_attachment=True, download_name="downtime_data.xlsx", mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

if __name__ == "__main__":
   app.run(debug=True)
