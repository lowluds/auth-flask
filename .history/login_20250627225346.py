from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
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
                    session['group'] = user['group'] 
                    # Redirect based on group
                    if user['group'] == 'admin':
                        return redirect(url_for('admin'))
                    else:
                        return redirect(url_for('dashboard'))
                else:
                    return "Incorrect password"
        
        return "User not found"

    return render_template('login.html')

@app.route('/register', methods=['GET', "POST"])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        group = request.form['group']

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Load existing users
        with open('userDB.json', 'r') as file:
            data = json.load(file)

        # Check for duplicate name
        for user in data['users']:
            if user['username'] == username:
                error = "Username already exists. Please choose another."
                return render_template(
                    'register.html',
                    error=error,
                    username=username,
                    group=group
                )   
        
        # Add new user to userDB.json
        data['users'].append({
            'username': username,
            'password': hashed_password,
            'group'   : group
        })

        # Save the updated user list to userDB.json
        with open('userDB.json', "w") as file:
            json.dump(data, file, indent=4)

    flash("You are registered! Please log in.", "Success")
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    # Check if user is logged in
    if 'username' in session:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))

@app.route('/admin')
def admin():
    if 'username' in session: 
        if session.get('group') == 'admin':
            return render_template('admin.html')
        else:
            return "You are logged in, but not authorized to view this page"
    else:    
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)