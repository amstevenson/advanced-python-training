import os
basedir = os.path.abspath(os.path.dirname(__file__))

# This file should be used only for containing environment variables, nothing else
APP_NAME = os.environ["APP_NAME"] = "python_training"
COMMIT = os.environ["COMMIT"] = "LOCALE"
LOG_LEVEL = os.environ["LOG_LEVEL"] = "DEBUG"
os.environ["PYTHONUNBUFFERED"] = "yes"

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                          'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
