import requests


class CategoryClient(object):

    @staticmethod
    def _get_category(url):
        """
        Retrieve json for a given category indicated by the url parameter
        :param url: The parameter determining what category will be retrieved from swapi
        :return: The json representation of the category
        """
        headers = {'Content-Type': 'application/json'}
        response_category = requests.get(url, headers=headers)
        response_category.raise_for_status()
        response_category_json = response_category.json()
        return response_category_json

    def get_planet(self, number):
        """
        Sends a request to swapi to return the json representation of a planet
        :param number: The number of the planet to be queried
        :return: The json representation of the requested planet
        """
        url_str = 'https://swapi.co/api/planets/{}'
        url = url_str.format(number)
        return self._get_category(url)

    def get_person(self, number):
        """
        Sends a request to swapi to return the json representation of a person
        :param number: The number of the person to be queried
        :return: The json representation of the requested person
        """
        url_str = 'https://swapi.co/api/people/{}'
        url = url_str.format(number)
        return self._get_category(url)
