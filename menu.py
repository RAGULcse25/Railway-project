from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("template.html")

@app.route('/reservation')
def reservation():
    return "Make Reservation Page"

@app.route('/employee')
def employee_login():
    return "Employee Login Page"

@app.route('/admin')
def admin():
    return "Admin Page"

if __name__ == '__main__':
    app.run(debug=True)