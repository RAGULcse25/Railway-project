# app.py
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a real secret key

# Dummy user data for demonstration
users = {
    "user@example.com": "password123"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = request.form.get('remember')

    # Check credentials (In real application, use proper database and password hashing)
    if email in users and users[email] == password:
        session['user'] = email
        if remember:
            session.permanent = True
        return redirect(url_for('dashboard'))
    return "Invalid credentials", 401

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('home'))
    return render_template('dashboard.html')  # Create this template

if __name__ == '__main__':
    app.run(debug=True)