from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allow frontend to call backend

@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.json
    print("Received data:", data)
    return jsonify({"message": "Signup successful!"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=5000)
