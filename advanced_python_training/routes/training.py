from flask import Blueprint, Response, render_template, request
from advanced_python_training.examples.final_exercise import weather_api
import logging
import json

training = Blueprint('training', __name__)

logger = logging.getLogger()


@training.route("/", methods=["GET"])
def index():
    return render_template('index.html')


@training.route("/weather", methods=["POST"])
def weather():
    city = request.form.get('city')
    country = request.form.get('country')
    weather_data = weather_api.WeatherGetter(city, country).getWeather()

    if not weather_data:
        return render_template('index.html', error=True)
    else:
        return render_template('index.html', temp=weather_data['main']['temp'],
                               lon=weather_data['coord']['lon'],
                               lat=weather_data['coord']['lat'])


@training.route("/get-weather-map", methods=["GET"])
def get_weather_map():
    lon = request.args.get('lon')
    lat = request.args.get('lat')
    return render_template('osm_map.html', lon=lon, lat=lat)


@training.route("/kitten", methods=["POST"])
def kitten():
    # Retrieve multiple kittens based on an amount between the min range and the max range
    min_range = request.form.get('minRange')
    max_range = request.form.get('maxRange')
    image_size = str(int((int(max_range)-int(min_range)) / 2))
    print('image size for kittens is {}'.format(image_size))
    return render_template('kitten.html', size=image_size)


@training.route("/list", methods=["GET"])
def list_examples():
    # May expand on this to call each example, for now it is a list
    return Response(response=json.dumps(
                    {'chapter 2': 'classes',
                     'chapter 3': 'decorators',
                     'chapter 4': 'simple logging example',
                     'chapter 5': 'regular expressions',
                     'chapter 6': 'multithreading. Queue example py is useful here.',
                     'chapter 7': 'Using new processes. Really good example for task queues',
                     'chapter 8': 'An example of constructing an email and sending it',
                     'chapter 9': 'Some unit testing examples',
                     'chapter 11': 'a rather rudimentary example of running a flask app (running app.py)',
                     'swapi_exercise': 'A sort of good example at running threads concurrently to call an '
                                       'api; Run main.py.',
                     'final_exercise': 'adding routes to a flask app (I am using my own) to add a call to '
                                       'a weather api, a kitten api and to modify data on a map.'}),
                    mimetype='application/json',
                    status=200)


@training.route("/test-page/<username>", methods=["GET"])
def test_page(username):
    print(username)
    return render_template('test_page.html', name=username)
