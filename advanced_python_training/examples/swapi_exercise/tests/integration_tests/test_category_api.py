import unittest
from advanced_python_training.examples.swapi_exercise.swapi.category_api_client import CategoryClient


class TestBank(unittest.TestCase):

    def setUp(self):
        self.client = CategoryClient()

    def test_get_planet(self):
        expected_planets = ['Tatooine', 'Alderaan', 'Yavin IV']
        for i in range(1, 4):
            planet = self.client.get_planet(i)
            self.assertEqual(planet['name'], expected_planets[i-1])

    def test_get_people(self):
        expected_people = ['Luke Skywalker', 'C-3PO', 'R2-D2']
        for i in range(1, 4):
            planet = self.client.get_person(i)
            self.assertEqual(planet['name'], expected_people[i-1])
