"""A simple flask web app"""
from flask import Flask, request
from flask import render_template
from calc.calculator import Calculator

app = Flask(__name__)


@app.route("/")
def index():
    """index  Route Response"""
    return render_template('index.html')


@app.route("/basicform", methods=['GET', 'POST'])
def basicform():
    """Post Request Handling"""
    if request.method == 'POST':
        # get the values out of the form
        value_a = request.form['value1']
        value_b = request.form['value2']
        operation = request.form['operation']
        getattr(Calculator, operation)(value_a, value_b)
        result = str(Calculator.last_calculation_result_in_history())
        return render_template('result.html', value1=value_a, value2=value_b, operation=operation, result=result)
    # Displays the form because if it isn't a post it is a get request
    else:
        return render_template('basicform.html')


@app.route("/bad/<value_a>/<value_b>")
def bad_calc(value_a, value_b):
    """bad calc Route Response"""
    result = value_a + value_b
    response = "The result of the calculation is: " + result + '<a href="/"> back</a>'
    return response


@app.route("/good/<float:value_a>/<float:value_b>")
def good_calc(value_a, value_b):
    """good calc Route Response"""
    my_tuple = (value_a, value_b)
    Calculator.addition(my_tuple)
    response = "The result of the calculation is: " + str(Calculator.last_calculation_result_in_history()) + '<a href="/"> back</a>'
    return response
