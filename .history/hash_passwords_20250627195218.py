from werkzeug.security import generate_password_hash, check_password_hash
import json

# Load JSON
with open('userDB.json', 'r') as file:
    data = json.load(file)

# Hash passwords
for user in data['users']:
    plain = user['password']
    user['password'] = generate_password_hash(plain)

# Save updated data back to the file
with open('userDB.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Passwords hashed and saved.")
