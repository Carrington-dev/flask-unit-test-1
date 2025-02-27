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

@app.route('/subtract', methods=['GET'])
def subtract_numbers():
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
        return jsonify({'result': num1 - num2})
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/multiply', methods=['GET'])
def multiply_numbers():
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
        return jsonify({'result': num1 * num2})
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/divide', methods=['GET'])
def divide_numbers():
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 1))
        if num2 == 0:
            return jsonify({'error': 'Cannot divide by zero'}), 400
        return jsonify({'result': num1 / num2})
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)
