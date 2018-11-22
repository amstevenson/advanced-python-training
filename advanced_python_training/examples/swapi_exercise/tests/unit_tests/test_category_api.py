import unittest
from advanced_python_training.examples.swapi_exercise.swapi.category_api_client import CategoryClient
import mock


class TestBank(unittest.TestCase):

    @mock.patch("python_training.examples.swapi_exercise.swapi.category_api_client.CategoryClient.get_planet")
    def test_get_planet(self, mock_client):
        mock_client.return_value = {'name': 'nug'}
        planet = CategoryClient().get_planet(2)['name']
        self.assertEqual(planet, 'nug')
        mock_client.assert_called_once_with(2)

    @mock.patch("python_training.examples.swapi_exercise.swapi.category_api_client.CategoryClient.get_person")
    def test_get_planet(self, mock_client):
        mock_client.return_value = {'name': 'nug'}
        planet = CategoryClient().get_person(2)['name']
        self.assertEqual(planet, 'nug')
        mock_client.assert_called_once_with(2)
