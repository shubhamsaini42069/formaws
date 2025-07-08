from flask import Flask, request, jsonify
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

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
