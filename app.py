from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Flask App'})

@app.route('/add', methods=['GET'])
def add_numbers():
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
        return jsonify({'result': num1 + num2})
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)
