#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:str>')
def print_string(str):
    print(f'{str}')
    return f'{str}'

@app.route('/count/<int:num>')
def count_int(num):
    count = f''
    for n in range(num):
        count += f'{n}\n'
    return count

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def calculate(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)
    else:
        return "Invalid operation"
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)