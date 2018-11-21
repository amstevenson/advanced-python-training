import time
from python_training.examples.swapi_exercise.swapi.category_api_client import CategoryClient
from python_training.examples.swapi_exercise.logger import logger
from python_training.examples.swapi_exercise.swapi.category_thread import CategoryThread


def main():
    start = time.time()
    category_client = CategoryClient()

    logger.info('Getting categories unthreaded')
    for i in (range(1, 4)):
        logger.debug('Getting planet number {} name'.format(i))
        planet_json = category_client.get_planet(i)
        logger.debug('Planet number {} name is: {}'.format(i, planet_json['name']))

    for i in (range(1, 4)):
        logger.debug('Getting person number {} name'.format(i))
        person_json = category_client.get_person(i)
        logger.debug('Planet number {} name is: {}'.format(i, person_json['name']))

    end = time.time()

    logger.info("Unthreaded Categories received in {} seconds \n".format(end-start))

    logger.info('Getting categories threaded')

    start = time.time()

    thread_list = ["Thread-1", "Thread-2", "Thread-3"]
    threads = []
    thread_id = 1

    # Create new threads
    # planets
    for tName in thread_list:
        thread = CategoryThread(thread_id, tName, thread_id, 'planet', category_client)
        thread.start()
        threads.append(thread)
        thread_id += 1

    # people
    for tName in thread_list:
        thread = CategoryThread(thread_id, tName, thread_id, 'person', category_client)
        thread.start()
        threads.append(thread)
        thread_id += 1

    # Wait for all threads to complete
    for t in threads:
        t.join()

    end = time.time()

    logger.info("Threaded Categories received in {} seconds \n".format(end-start))

if __name__ == '__main__':
    main()
