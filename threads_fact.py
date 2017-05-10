import threading
from prime_factorization import *
from utils import miller_rabin_test


class facthreads (threading.Thread):
    def __init__(self, func, n, name):
        threading.Thread.__init__(self)
        self.func = func
        self.n = n
        self.name = name

    def run(self):
        print(self.name, str(self.func(self.n)))

def compute(n):
    #first check if prime
    if miller_rabin_test(n):
        print("El numero el primo!")
        return
    # Create new threads
    thread1 = facthreads(fermat, n, 'fermat:')
    thread2 = facthreads(pollards_rho, n, 'rho:')
    thread3 = facthreads(pollards_pm1, n, 'pm1:')
    thread4 = facthreads(fermat_decimal, n, 'fermat_Dec:')


    # Start new Threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    '''
    thread1.join()
    thread2.join()
    thread3.join()
    '''
