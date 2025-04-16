# app.py
from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

# Ensure the data directory exists
os.makedirs('data', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'phone': request.form['phone'],
        'address': request.form['address'],
        'username': request.form['username'],
        'email': request.form['email']
    }

    # Save to CSV file
    with open('data/passengers.csv', 'a', newline='') as csvfile:
        fieldnames = data.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header if file is empty
        if csvfile.tell() == 0:
            writer.writeheader()
        
        writer.writerow(data)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)