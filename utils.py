'''
This class provides functions that can be
usefull in cryptanalysis

Vicent Blanes <viblasel@gmail.com>
'''

import random

def simple_is_prime(n):
    """
    Returns True if n is prime.
    Useless for big numbers
    """
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

'''
Functions for Miller-Rabin test
'''

def decompose(n):
   exponentOfTwo = 0

   while n % 2 == 0:
      n = n/2
      exponentOfTwo += 1

   return exponentOfTwo, n

def isWitness(possibleWitness, p, exponent, remainder):
   possibleWitness = pow(possibleWitness, remainder, p)
   if possibleWitness == 1 or possibleWitness == p - 1:
      return False

   for _ in range(exponent):
      possibleWitness = pow(possibleWitness, 2, p)

      if possibleWitness == p - 1:
         return False

   return True

def miller_rabin_test(p, accuracy=100):
   if p == 2 or p == 3: return True
   if p < 2: return False

   exponent, remainder = decompose(p - 1)

   for _ in range(accuracy):
      possibleWitness = random.randint(2, p - 2)
      if isWitness(possibleWitness, p, exponent, remainder):
         return False

   return True
