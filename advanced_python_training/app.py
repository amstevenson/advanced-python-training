from flask import Flask
from advanced_python_training.logconfig import register_logging
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

register_logging()
app = Flask(__name__)
app.config.from_pyfile("config.py")
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from advanced_python_training import models