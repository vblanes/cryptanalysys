from prime_factorization import *

p = 2750159
q = 373587883
n = p*q
#print(fermat(n))
#print(pollards_rho(n))
print(pollards_pm1(n))
