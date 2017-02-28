import logging

from flask import Flask, redirect


app = Flask(__name__)

@app.route('/')
def index():
    return redirect('https://github.com/zqureshi/snippets')

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during the request.')
    return 'An internal error occurred.', 500
