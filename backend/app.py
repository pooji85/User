# Filename: app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Folder to save uploaded resumes
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return "Flask backend is running!"

# ---------------------- GET ROUTE ----------------------
@app.route('/get-users', methods=['GET'])
def get_users():
    # Dummy response for GET request
    users = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Emma"},
        {"id": 3, "name": "Alex"}
    ]
    return jsonify({"status": "success", "users": users}), 200

# ---------------------- POST ROUTE ----------------------
@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.form.to_dict()
    print("Form Data:", data)

    # Handle file (resume)
    file = request.files.get('resume')
    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        print("File saved:", file_path)

    response = {
        "status": "success",
        "message": "Form data received successfully",
        "data": data
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)   # Required for Docker + EC2
