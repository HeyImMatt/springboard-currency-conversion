from flask import Flask, redirect, request, render_template, flash, jsonify, Response, url_for
from flask_debugtoolbar import DebugToolbarExtension
from handlers import form_validate
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
        amount = request.form['amount']
        validation_message = form_validate(from_code, to_code, amount)

        if validation_message != True:
            flash(validation_message)
            return redirect('/')

        exchange_rate = get_rate(from_code, to_code, float(amount))
        return redirect(url_for('rate', exchange_rate=exchange_rate))

    return render_template('index.html')


@app.route('/rate', methods=['GET', 'POST'])
def rate():
    if request.method == 'POST':
        return redirect('/')

    exchange_rate = request.args.get('exchange_rate')
    return render_template('rate.html', exchange_rate=exchange_rate)
