import multiprocessing
import time


def hello():
    name = multiprocessing.current_process().name
    print('starting my process')
    print(name, 'says hello world')
    print('started {}'.format(multiprocessing.current_process()))
    time.sleep(3)
    print('process terminating')


if __name__ == '__main__':

    print('Main process {}'.format(multiprocessing.current_process()))
    myProcess = multiprocessing.Process(target=hello, name='my process')
    # myProcess.daemon = True  # Kills any sub procs (children) on end
    #                          # Not good for database calls etc, as it can be interruptable

    myProcess.start()

    print('the main process carries on as normal')
    time.sleep(7)

