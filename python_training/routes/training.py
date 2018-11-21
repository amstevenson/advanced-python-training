from flask import Blueprint, Response
from python_training.examples.ch2Classes import call_example
import logging
import json

training = Blueprint('training', __name__)

logger = logging.getLogger()


@training.route("/", methods=["GET"])
def index():
    return Response(response=json.dumps('test'),
                    mimetype="application/json",
                    status=200)


@training.route("/chapter_2", methods=["GET"])
def chapter_2():
    return call_example()
