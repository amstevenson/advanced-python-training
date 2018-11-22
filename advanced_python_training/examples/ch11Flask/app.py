"""
Note, this is another example of a standalone way to run a flask server
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'this is the home page'


@app.route('/welcome')
def welcome():
    return '<h1>Welcome</h1>'


@app.route('/greeting')
@app.route('/greeting/<name>')
def greeting(name=None):
    return 'empty' if not name else name

if __name__ == '__main__':
    app.run(port=5050)
