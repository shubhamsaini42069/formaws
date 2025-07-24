from flask import Flask, request, jsonify,requests
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
submitted_data = []

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    
    # Save to the list
    submitted_data.append({'name': name, 'email': email})
    
    return jsonify({'message': f'got your name {name} ({email})'})

@app.route('/view', methods=['GET'])
def view():
    return jsonify(submitted_data)
@app.route('/')
def index():
    return "AWS Flask App is running!"
@app.route('/get-ip')
def get_ip():
    ip = requests.get("http://169.254.169.254/latest/meta-data/public-ipv4").text
    return jsonify({"ip": ip})


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
