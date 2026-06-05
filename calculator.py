from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    try:
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        operation = data['operation']

        if operation == 'add':
            result = num1 + num2
            symbol = '+'
        elif operation == 'subtract':
            result = num1 - num2
            symbol = '−'
        elif operation == 'multiply':
            result = num1 * num2
            symbol = '×'
        elif operation == 'divide':
            if num2 == 0:
                return jsonify({'error': 'Cannot divide by zero'}), 400
            result = num1 / num2
            symbol = '÷'
        else:
            return jsonify({'error': 'Invalid operation'}), 400

        if result == int(result):
            result_str = str(int(result))
        else:
            result_str = f"{result:.6f}".rstrip('0')

        return jsonify({
            'result': result_str,
            'expression': f"{num1:g} {symbol} {num2:g} = {result_str}"
        })

    except (ValueError, KeyError):
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)
