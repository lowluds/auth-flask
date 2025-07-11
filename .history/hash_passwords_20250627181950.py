from werkzeug.security import generate_password_hash, check_password_hash
import json

# Load JSON
with open('userDB.json', 'r') as file:
    data = json.load(file)

for user in data['users']:
    plain = user['password']
    user['password'] =  generate_password_hash(plain)
