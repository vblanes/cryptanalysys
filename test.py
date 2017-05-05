from prime_factorization import *
from utils import simple_is_prime as sip
from threads_fact import compute
p = 2750159
q = 373587883
n = p*q
rsa100 = 1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139
rsa110 = 35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516111204504060317568667
#print(fermat(n))
#print(pollards_rho(n))
#print(pollards_pm1(n))
#print(sip(n**10))
compute(n)
