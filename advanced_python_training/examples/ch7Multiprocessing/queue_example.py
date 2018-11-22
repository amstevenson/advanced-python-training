# From https://pymotw.com/3/multiprocessing/communication.html
import multiprocessing
from advanced_python_training.examples.ch7Multiprocessing.consumer import Consumer
from advanced_python_training.examples.ch7Multiprocessing.Task import Task

if __name__ == '__main__':
    # Establish communication queues
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    # Start consumers
    num_consumers = multiprocessing.cpu_count() * 2
    print('Creating {} consumers'.format(num_consumers))
    consumers = [
        Consumer(tasks, results)  # empty queue upon declaration here of tasks
        for i in range(num_consumers)
        ]
    for w in consumers:
        w.start()

    # Enqueue jobs
    num_jobs = 10
    for i in range(num_jobs):
        tasks.put(Task(i, i))  # this is where we are putting work onto the task queue

    # Add a poison pill for each consumer - this will end the process
    for i in range(num_consumers):
        tasks.put(None)

    # Wait for all of the tasks to finish
    tasks.join()

    # Start printing results
    while num_jobs:
        result = results.get()
        print('Result:', result)
        num_jobs -= 1
