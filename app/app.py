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
        if request.form.get('action') == 'Clear':
            Calculator.clear_csv_files()
            return render_template('result.html', value1="", value2="", operation="", result="")
        # get the values from the form
        value_a = request.form['value1']
        value_b = request.form['value2']
        operation = request.form['operation']
        # flash message for empty input field error
        if value_a == "" or value_b == "":
            flash("Empty Input Field Error! You must input a numeric value for both Value 1 and Value 2!", "error")
            result = "error"
            Calculator.read_csv_file()
            items = Calculator.get_history()
            return render_template('result.html', value1=value_a, value2=value_b, operation=operation, items=items, result=result)
        # do regular calculation if there are no errors
        else:
            getattr(Calculator, operation)(value_a, value_b)
            result = str(Calculator.last_calculation_result_in_history())
            Calculator.put_history_to_csv(operation, value_a, value_b, result)
            Calculator.read_csv_file()
            items = Calculator.get_history()
            return render_template('result.html', value1=value_a, value2=value_b, operation=operation, items=items, result=result)
    else:
        return render_template('basicform.html')

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
