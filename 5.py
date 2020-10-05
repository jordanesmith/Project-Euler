'''project euler task 5'''
'''calculate lowest common multiple of 2,3,4...19,20'''
from task_3 import prime_factors
import numpy as np

biggest_number = 20
list_prime_factors = []
prime_dict = {}

for i in range(2,biggest_number+1):
    prime_dict[i] = np.array(prime_factors(i))
    for prime in prime_factors(i):
        list_prime_factors.append(prime)

list_prime_factors = list(set(list_prime_factors))
no_prime_occurance = {}
for prime in list_prime_factors:
    no_prime_occurance[prime] = 1

for i,list_primes in enumerate(prime_dict.values()):
    i+=2
    if list_primes.shape != (1,):
        for prime in list_prime_factors:
            no_occurances = sum(map(lambda x : x/prime == 1, list_primes))
            if no_occurances > no_prime_occurance[prime]:
                no_prime_occurance[prime] = no_occurances

print(no_prime_occurance)

final_answer = 1

for prime in list_prime_factors:
    final_answer *= prime**(no_prime_occurance[prime])

print(final_answer)

