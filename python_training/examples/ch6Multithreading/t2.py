import sys
import time
import random

from threading import Thread

# event is more than locking, something discernable on a global scale where information can be attached

# semaphore signal between threads, so they can determine what to respond to

# locks are simple if all we need is to lock and unlock based on context only within a thread


# Create a runnable class
class MyClass(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        for i in range(1, 50):
            sys.stdout.write(self.name)
            time.sleep(random.random() * 0.1)

if __name__ == '__main__':
    m1 = MyClass("1")
    m2 = MyClass("2")

    # run
    m1.start()  # start invokes the run method and __init__ creates the thread
    m2.start()

    # wait until complete
    m1.join()
    m2.join()
