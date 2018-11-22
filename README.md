# python-training

Advanced python training course, exercises contained within the examples folder are from the course

The entire application outside of the exercises folder demonstrates a simple flask example that I have made that will give me 
a list of what has been offered on this course, as well as a simple database example in the training route. 

A super simple example of creating a flask app can be found in the flask section of the examples folder (simply run app.py)

## Running

For running the outside flask application:

### Virtualenv

1) Virtualenv venv
2) source venv/Scripts/activate - for windows 
    or source venv/bin/activate - mac
    - type deactivate to close
3) flask db init (if not already done)
4) flask db upgrade (if not already done)
5) install dependencies (can use requirements.txt for this)
    - if you get a pip error, try `curl https://bootstrap.pypa.io/get-pip.py | python`
    - you will need to install the database using flask db init 
        - If this does not work, deactivate and uninstall flask, source into venv and pip install sqlalchemy and migrate. Command should appear after that. 

6) set FLASK_APP variable with
    "set FLASK_APP=manage.py" (for windows)
    or "export FLASK_APP=manage.py" (for mac)
7) flask run

### Docker (still a work in progress)

With purely docker (go to main directory):

1) docker build -t python_training .
2) docker run -p 8080:80 python_training

### Example ORM requests (using 'game' blueprint/routes)

## Add a  game

`curl -X POST -d '{"name": "ok", "rating": "6", "genre": "test"}' -H 'Content-Type: application/json' http://localhost:5000/add-game`

