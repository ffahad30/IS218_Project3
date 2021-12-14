"""A simple flask web app"""
from flask import Flask, request
from flask import render_template
from flask import flash
from calc.calculator import Calculator
app = Flask(__name__)

@app.route("/")
def index():
    """index Route Response"""
    return render_template("index.html")

@app.route("/basicform", methods=['GET', 'POST'])
def basicform():
    """Post Request Handling"""
    # Successful Calculation
    if request.method == 'POST':
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = request.form['operation']
        my_tuple = (value1, value2)
        getattr(Calculator, operation)(my_tuple)
        result = str(Calculator.last_calculation_result_in_history())
        return render_template("result.html", value1=value1, value2=value2, operation=operation, result=result)
    # Displays the form because if it isn't a post it is a get request
    else:
        return render_template("basicform.html")
