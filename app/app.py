"""A simple flask web app"""
from flask import Flask, request, flash
from flask import render_template
from calc.calculator import Calculator
from werkzeug.debug import DebuggedApplication

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)


@app.route("/")
def index():
    """index Route Response"""
    return render_template('index.html')


@app.route("/basicform", methods=['GET', 'POST'])
def basicform():
    """Post Request Handling"""
    if request.method == 'POST':
        # get the values from the form
        value_a = request.form['value1']
        value_b = request.form['value2']
        operation = request.form['operation']
        # flash message for empty input field error
        if value_a == "" or value_b == "":
            flash("Empty Input Field Error! You must input a numeric value for both Value 1 and Value 2!", "error")
            result = "error"
            return render_template('result.html', value1=value_a, value2=value_b, operation=operation, result=result)
        # do regular calculation if there are no errors
        else:
            getattr(Calculator, operation)(value_a, value_b)
            result = str(Calculator.last_calculation_result_in_history())
            return render_template('result.html', value1=value_a, value2=value_b, operation=operation, result=result)
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
    response = "The result of the calculation is: " + str(
        Calculator.last_calculation_result_in_history()) + '<a href="/"> back</a>'
    return response
