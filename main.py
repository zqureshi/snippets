import logging

from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return 'https://github.com/zqureshi/snippets', 302

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during the request.')
    return 'An internal error occurred.', 500
