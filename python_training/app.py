from flask import Flask
from python_training.logconfig import register_logging

register_logging()
app = Flask(__name__)
app.config.from_pyfile("config.py")
