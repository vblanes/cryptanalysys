'''
Cryptanalysis for public-key methods
based on primes factorization

Vicent Blanes <viblasel@gmail.com>
'''
from decimal import *
from math import ceil, sqrt, gcd
from random import randint
from numba import jit


@jit
def fermat(n):
    '''
    Require: N, product of 2 primes
    Ensure: Factors A and B from N
    Recomended if factors values are close
    '''
    n = Decimal(n)
    a = n.sqrt().to_integral_exact()
    b = (a**2)-n
    # while b is not a perfect square
    while not (b.sqrt() % 1 == 0):
        a += 1
        b = (a**2)-n
    return a-int(b.sqrt())

@jit
def pollards_rho(n):
    '''
    Require: N, product of 2 primes
    Ensure: P, one of the factors of N
    '''
    a = b = 2
    while True:
        a = (a**2+1) % n
        b = (b**2+1) % n
        b = (b**2+1) % n
        p = gcd(a-b, n)
        if p > 1 and p <= n:
            return p
@jit
def pollards_pm1(n):
    '''
    Require: N, product of 2 primes
    Ensure: one of the factors of N
    '''
    #random integer 2 <= a <= n-1
    a = randint(2, n-1)
    aux = gcd(a, n)
    # if 1 < random < n
    if aux > 1 and aux < n:
        return aux
    k = 2
    while True:
        #powermod
        a = pow(a, k, n)
        d = gcd(a-1, n)
        # if 1 < d < n then return d
        if d > 1 and d < n:
            return d
        if d == n:
            return None
        k += 1
