# Auth Flask

A simple user authentication system built with Flask. It includes login, registration, password hashing, and a demo "Forgot Password" page. This project is designed as a minimal yet functional starting point for user authentication in a Python web app.

## Features

* User login and registration
* Passwords securely hashed using `werkzeug.security`
* JSON file used as a lightweight user database
* Flash messages for login feedback
* Clean UI using custom CSS
* Demo-only "Forgot Password" page (non-functional placeholder)

## How to Run

1. Make sure you have Python installed (3.8+ recommended).
2. Install Flask if you haven’t already:

   ```bash
   pip install flask
   ```
3. Run the app:

   ```bash
   python login.py
   ```
4. Open your browser and go to:
   (http://127.0.0.1:5000)

## Notes

* Newly registered users have their passwords automatically hashed using `werkzeug.security`.
* You can also manually add users to `userDB.json`. If doing so, run `hash_passwords.py` to hash any plaintext passwords before login.
* The "Forgot Password" page is a non-functional placeholder and does not include email recovery or reset features.

## Project Structure

```
AUTH-FLASK/
│
├── static/                 # CSS stylesheets
│   ├── admin.css
│   ├── error.css
│   ├── flash.css
│   ├── register.css
│   └── style.css
│
├── templates/              # HTML templates for Flask
│   ├── admin.html
│   ├── dashboard.html
│   ├── forgot.html
│   ├── login.html
│   └── register.html
│
├── users/                  # User data storage
│   └── userDB.json
│
├── .gitignore              # Git ignored files
├── hash_passwords.py       # One-time script to hash plaintext passwords
├── login.py                # Main Flask application
└── README.md               # Project documentation
```