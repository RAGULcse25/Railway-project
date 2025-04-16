from flask import Flask, render_template
import polars as pl

app = Flask(__name__)

def get_train_data():
    # Read Excel file using Polars
    try:
        df = pl.read_excel('E:\railway pro\train_schedule.xlsx')
        # Convert to list of dictionaries for HTML rendering
        trains = df.to_dicts()
        
        # Add status classes and format currency
        for train in trains:
            train['status_class'] = 'on-time' if train['Status'] == 'On Time' else 'delayed'
            train['Fare'] = f"₹{train['Fare']:,.2f}"
        
        return trains
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return []

@app.route('/')
def dashboard():
    trains = get_train_data()
    return render_template('dashboard.html', trains=trains)

if __name__ == '__main__':
    app.run(debug=True, port=5000)