"""A simple flask web app"""
from flask import Flask, request, flash
from flask import render_template
from werkzeug.debug import DebuggedApplication
from calc.calculator import Calculator


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)
# pylint: disable="line-too-long"
# pylint: disable="no-else-return"

@app.route("/")
def index():
    """index Route Response"""
    return render_template('index.html')

@app.route("/pylint")
def pylint():
    """Pylint Route Response"""
    return render_template('pylint.html')

@app.route("/aaa")
def aaa():
    """AAA Route Response"""
    return render_template('aaa.html')

@app.route("/oop")
def oop():
    """OOP Route Response"""
    return render_template('oop.html')

@app.route("/solid")
def solid():
    """SOLID Route Response"""
    return render_template('solid.html')

@app.route("/basicform", methods=['GET', 'POST'])
def basicform():
    """Post Request Handling"""
    if request.method == 'POST':
        if request.form.get('action') == 'Clear':
            Calculator.clear_history_csv()
            return render_template('result.html', value1="", value2="", operation="", result="")
        # get the values from the form
        value_a = request.form['value1']
        value_b = request.form['value2']
        operation = request.form['operation']
        # flash message for empty input field error
        if value_a == "" or value_b == "":
            flash("Empty Input Field Error! You must input a numeric value for both Value 1 and Value 2!", "error")
            result = "error"
            Calculator.read_history_csv()
            calculation_info = Calculator.return_calc_history()
            return render_template('result.html', value1=value_a, value2=value_b, operation=operation, result=result, calculation_info=calculation_info,)
        # do regular calculation if there are no errors
        else:
            getattr(Calculator, operation)(value_a, value_b)
            result = str(Calculator.last_calculation_result_in_history())
            Calculator.write_history_csv(value_a, value_b, operation, result)
            Calculator.read_history_csv()
            calculation_info = Calculator.return_calc_history()
            return render_template('result.html', value1=value_a, value2=value_b, operation=operation, result=result, calculation_info=calculation_info)
    else:
        return render_template('basicform.html')
