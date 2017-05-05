import threading
from prime_factorization import *


class facthreads (threading.Thread):
    def __init__(self, func, n, name):
        threading.Thread.__init__(self)
        self.func = func
        self.n = n
        self.name = name

    def run(self):
        print(self.name, str(self.func(self.n)))

def compute(n):
    # Create new threads
    thread1 = facthreads(fermat, n, 'fermat:')
    thread2 = facthreads(pollards_rho, n, 'rho:')
    thread3 = facthreads(pollards_pm1, n, 'pm1:')

    # Start new Threads
    thread1.start()
    thread2.start()
    thread3.start()
    '''
    thread1.join()
    thread2.join()
    thread3.join()
    '''
