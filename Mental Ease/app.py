from flask import Flask, request
import secrets

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_account_number():
    n = secrets.token_hex(6)
    n = int(n, 16)
    return str(n)

if __name__ == "__main__":
    app.run(port=5000)
