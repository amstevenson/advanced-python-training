from advanced_python_training.app import app
from advanced_python_training.blueprints import register_blueprints

# The starting point of the application. Referenced by manage.py
# Imports it and then initialises blueprints against imported app
register_blueprints(app)
