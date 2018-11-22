from flask import Blueprint, Response, render_template
import logging
import json

training = Blueprint('training', __name__)

logger = logging.getLogger()


@training.route("/test/<username>", methods=["GET"])
def index(username):
    return Response(response=json.dumps({'username': username}),
                    mimetype="application/json",
                    status=200)


@training.route("/list", methods=["GET"])
def list():
    # May expand on this to call each example, for now it is a list
    return Response(response=json.dumps(
                    {'chapter 2': 'classes',
                     'chapter 3': 'decorators',
                     'chapter 4': 'simple logging example',
                     'chapter 5': 'regular expressions',
                     'chapter 6': 'multithreading. Queue example py is useful here.',
                     'chapter 8': 'An example of constructing an email and sending it',
                     'chapter 9': 'Some unit testing examples',
                     'chapter 11': 'a rather rudimentary example of running a flask app (running app.py)',
                     'swapi_exercise': 'A sort of good example at running threads concurrently to call an '
                                       'api; Run main.py.'}),
                    mimetype='application/json',
                    status=200)


@training.route("/test-page/<username>", methods=["GET"])
def test_page(username):
    print(username)
    return render_template('test_page.html', name=username)
