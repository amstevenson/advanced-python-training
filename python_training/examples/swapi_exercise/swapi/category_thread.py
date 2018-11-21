import threading
from python_training.examples.swapi_exercise.logger import logger


class CategoryThread(threading.Thread):
    def __init__(self, thread_id, name, number, category, client):
        """

        Initialiser for the thread that will retrieve a provided category

        :param thread_id: The threads id
        :param name: The name of the thread
        :param number: The number of the category to be collected, this will be
                        determined by the thread id, which will go from 1 to 3
        :param category: the category
        :param client: The client responsible for sending requests to swapi
        """
        super().__init__()
        self.threadID = thread_id
        self.name = name
        self.number = number
        self.category = category
        self.client = client

    def run(self):
        """
        The runnable for the thread. In this instance, it will call swapi and list each
        retrieved planet.
        """
        logger.debug('Getting {} number {} name'.format(self.category, self.number))
        category_json = self.client.get_planet(self.number) if self.category == 'planet' else \
            self.client.get_person(self.number)

        logger.debug('category {} number {} name is: {}'.format(self.category, self.number, category_json['name']))
        return category_json
