import os

# This file should be used only for containing environment variables, nothing else
APP_NAME = os.environ["APP_NAME"] = "python_training"
COMMIT = os.environ["COMMIT"] = "LOCALE"
LOG_LEVEL = os.environ["LOG_LEVEL"] = "DEBUG"
os.environ["PYTHONUNBUFFERED"] = "yes"
