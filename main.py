from flask import Flask

app = Flask(__name__)

operations = ('+', ':', '**', '-', '*') # Используемые арифметические операторы для этого задания

@app.route("/<string:num>/")
def next(num):
    a = int(num[0])
    b = int(num[-1])
    if num[1] == '+':
        return f"{a + b}"
    elif num[1] == '-':
        return f"{a - b}"
    elif num[1] == '*' and len(num) == 3:
        return f"{a * b}"
    elif num[1] == ':':
        return f"{a / b}"
    elif num[1:3] == '**' and len(num) == 4:
        return f"{a ** b}"