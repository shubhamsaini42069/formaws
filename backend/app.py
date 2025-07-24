from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

submitted_data = []

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    
    submitted_data.append({'name': name, 'email': email})
    return jsonify({'message': f'Got your name {name} ({email})'})

@app.route('/view', methods=['GET'])
def view():
    return jsonify(submitted_data)

@app.route('/')
def index():
    return "AWS Flask App is running!"

@app.route('/get-ip')
def get_ip():
    try:
        token = requests.put(
            "http://169.254.169.254/latest/api/token",
            headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"}
        ).text

        ip = requests.get(
            "http://169.254.169.254/latest/meta-data/public-ipv4",
            headers={"X-aws-ec2-metadata-token": token}
        ).text

        return jsonify({"ip": ip})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
