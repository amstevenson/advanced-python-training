# python-training

Advanced python training course, exercises contained within the examples folder

## Running

### Fastest way (standalone):

python3 ./manage.py runserver

### Virtualenv

1) Virtualenv venv
2) source venv/Scripts/activate - for windows
or source venv/bin/activate - mac
3) install dependencies (can use requirements.txt for this)
4) set FLASK_APP variable with
    "set FLASK_APP=manage.py" (for windows)
    or "export FLASK_APP=manage.py" (for mac)
5) flask run

### Docker (still a work in progress)

With purely docker (go to main directory):

1) docker build -t python_training .
2) docker run -p 8080:80 python_training
