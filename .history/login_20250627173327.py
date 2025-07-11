from flask import Flask, render_template, request, redirect, url_for, session

app = Flask (__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure random value

# In-memory user store for demonstration
users = {'testuser': 'testpass'}

@app.route('/')
def home():
    if 'username' in session:
        return f"Logged in as {session['username']} <a href='/logout'>Logout</a>"
    return "<a href='/login'>Login</a> | <a href='/register'>Register</a>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        return 'Invalid credentials!'
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return 'User already exists!'
        users[username] = password
        return redirect(url_for('login'))
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Register">
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
