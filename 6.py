from task_3 import prime_factors
import numpy as np
import pandas as pd

biggest_number = 100
list_prime_factors = []
numbers = range(1,biggest_number+1)

for i in range(2,biggest_number+1):
    for prime in prime_factors(i):
        list_prime_factors.append(prime)

list_prime_factors = list(set(list_prime_factors))

#create a datagram with number on y axies, and Prime factors
#along the x axis, and the contents are the number of time 
#each PF occurs in each number

df = pd.DataFrame(data=None, index=numbers, columns=list_prime_factors, dtype=int)

for number in numbers:
    list_primes = prime_factors(number)
    for prime in list_prime_factors:
        no_occurances = sum(map(lambda x : x/prime == 1, list_primes))
        df[prime][number] = no_occurances

print(df)

square_of_sum = sum(numbers)**2 
print(square_of_sum)

#create algorithm to sum the dataframe consecutively
def sum_dataframe(df):
    for row in df:
        print(row)

df_squares = df*2

sum_dataframe(df_squares)

