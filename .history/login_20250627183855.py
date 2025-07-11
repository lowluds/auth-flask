from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash
import json

app = Flask (__name__)
app.secret_key = '123abc456'  # Change this to a secure random value

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form input
        username = request.form['username']
        password = request.form['password']

    # Load users from JSON
    with open('userDB.json', 'r') as file:
        data = json.load(file)

    # Look for user
    for user in data['users']:
        if user['username'] == username:
            # Check hashed password
            if check_password_hash(user['password'], password):
                session['username'] = username
                return "Login Successful"
        else:
            return "Incorrect password"
    
        return "User not found"

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)


