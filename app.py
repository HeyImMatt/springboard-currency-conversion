from flask import Flask, redirect, request, render_template, flash, jsonify, Response
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = '1579'

debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route('/', methods=['GET', 'POST'])
def home_get_route():
    if request.method == 'POST': 
        return redirect('/rate')

    return render_template('index.html')

@app.route('/rate', methods=['GET', 'POST'])
def rate_get_route():
    if request.method == 'POST': 
        return redirect('/')
        
    return render_template('rate.html')