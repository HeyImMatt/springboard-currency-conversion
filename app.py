from flask import Flask, redirect, request, render_template, flash, jsonify, Response, url_for
from flask_debugtoolbar import DebugToolbarExtension
from forex import get_rate, validate_code

app = Flask(__name__)
app.config['SECRET_KEY'] = '1579'

debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        from_code = request.form['from-code'].upper() 
        to_code = request.form['to-code'].upper()
        amount = float(request.form['amount'])
        validation_message = form_validate(from_code, to_code)

        if validation_message != True:
            flash(validation_message)
            return redirect('/')

        exchange_rate = get_rate(from_code, to_code, amount)
        return redirect(url_for('rate', exchange_rate=exchange_rate))

    return render_template('index.html')

@app.route('/rate<exchange_rate>', methods=['GET', 'POST'])
def rate(exchange_rate):
    if request.method == 'POST': 
        return redirect('/')

    return render_template('rate.html', exchange_rate=exchange_rate)

def form_validate(from_code, to_code):
    if validate_code(from_code) == False:
        return 'From code not valid'
    
    if validate_code(to_code) == False:
        return 'To code not valid'

    return True