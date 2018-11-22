# python-training

Advanced python training course.

Training routes encompass material from the course that are contained within the examples folder. Everything outside 
of that folder is not related to the course with the exception of the final task, which involves me setting 
up some routes on this custom project I have made. 

Game route (ORM etc) encompasses me playing around with ORM and is separate to the course. 

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
    `set FLASK_APP=manage.py` (for windows)
    or `export FLASK_APP=manage.py` (for mac)
7) flask run
8) If any issues, can run `export FLASK_DEBUG=1` to debug

### Random kitten and weather requests using forms

### Example ORM requests (using 'game' blueprint/routes)

## Add a  game

`curl -X POST -d '{"name": "ok", "rating": "6", "genre": "test"}' -H 'Content-Type: application/json' http://localhost:5000/add-game`

## Get all games 

`curl localhost:5000/all-games`