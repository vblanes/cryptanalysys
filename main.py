'''
Using threads for getting better time in crypto competition :)
'''
import sys
from prime_factorization import *

opt = int(input("1) Fermat\n2) Rho\n3) PM1\n"))
n = int(input("Numero a factorizar\n"))

if opt == 1:
    print(fermat(n))
elif opt == 2:
    print(pollards_rho(n))
elif opt == 3:
    print(pollards_pm1(n))
