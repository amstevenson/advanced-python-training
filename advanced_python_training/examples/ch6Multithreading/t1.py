import sys
import time
import random

from threading import Thread


# call-back
def myfunc(name):
    for i in range(1, 50):
        sys.stdout.write(name)
        time.sleep(random.random() * 0.1)

if __name__ == '__main__':
    # define a callback functions - to be called via start
    thread1 = Thread(target=myfunc, args=("1",))  # comma is converting to a set (unique immutable values)
    thread2 = Thread(target=myfunc, args=("2",))

    # start the threads
    thread1.start()
    thread2.start()

    # wait for the threads to complete
    thread1.join()  # this will stop, return processing and will see results
    thread2.join()
