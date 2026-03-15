from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # allows frontend to fetch from a different port

@app.route("/api/sample")
def sample():
    return jsonify({"message": "Hello World! From the backend"})

if __name__ == "__main__":
    app.run(debug=True)