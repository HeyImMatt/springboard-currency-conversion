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
    '''Get route shows exchange form. Post route redirects to rate page if user input is valid'''
    if request.method == 'POST':
        from_code = request.form['from-code'].upper()
        to_code = request.form['to-code'].upper()
        amount = request.form['amount']
        validation = form_validate(from_code, to_code, amount)

        if validation != True:
            flash(validation)
            return redirect('/')

        converted_amount = get_rate(from_code, to_code, float(amount))
        
        if converted_amount == False:
            flash('Cannot convert. Conversion service down. 🙁')
            return redirect('/')

        return redirect(url_for('rate', converted_amount=converted_amount))

    return render_template('index.html')


@app.route('/rate', methods=['GET', 'POST'])
def rate():
    '''Get route displays exchange rate info. Post route redirects to homepage to start over.'''
    if request.method == 'POST':
        return redirect('/')

    converted_amount = request.args.get('converted_amount')
    return render_template('rate.html', converted_amount=converted_amount)
