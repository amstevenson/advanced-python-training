import requests
import time


class WeatherGetter(object):
    def __init__(self, city='plymouth', country='uk'):
        self.city = city
        self.country = country
        self.APIkey = 'APPID=48f2d5e18b0d2bc50519b58cce6409f1'

    def getWeather(self):
        url_str = 'http://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&{}'
        url = url_str.format(self.city, self.country, self.APIkey)
        data = requests.get(url).json()
        if 'main' in data:
            # self.temperature = data['main']['temp']
            return data


def main():
    start = time.time()
    weatherGetter = WeatherGetter()
    weather = weatherGetter.getWeather()
    print('Description: {} Temperature: {:.0f}°C in {}'.format(weather['weather'][0]['description'],
                                                               weather['main']['temp'], weather['name']))
    end = time.time()

    print("Weather received in {} seconds".format(end-start))

if __name__ == '__main__':
    main()
