from flask import Flask, jsonify
import random
import string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def generate_password(length, password_types):
    if not password_types:
        password_types = ['default']

    characters = ''
    if 'uppercase' in password_types:
        characters += string.ascii_uppercase
    if 'lowercase' in password_types:
        characters += string.ascii_lowercase
    if 'numeric' in password_types:
        characters += string.digits
    if 'symbols' in password_types:
        characters += "@$&*##"

    if not characters:
        characters = string.ascii_letters + string.digits + "@$&*#"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/password_length/<int:length>/<string:password_types>')
def generate_password_type(length, password_types):
    types = password_types.split(',')
    password = generate_password(length, types)
    return jsonify(password=password)

if __name__ == '__main__':
    app.run(debug=True,port=5000)
