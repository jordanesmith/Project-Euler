'''runs task 3'''
from task3 import factors, prime_numbers
import time
import numpy as np
import matplotlib.pyplot as plt


times = np.zeros(shape=(10,2))
print(times)
a = 0
for i in range(0,10):
    start = time.time()
    power = int(i)
    a = 10**power
    odd_numbers = []
    square_numbers = []
    for i in range(int(a/2)): #create list of odd numbers in range needed
        if i <= int((a**0.5)+1):
            square_numbers.append(i**2)
        if i%2 != 0:
            odd_numbers.append(i)
    prime_numbers(a)    
    end = time.time()
    time_taken = end - start
    times[i,0],times[i,1] = i, time_taken


plt.plot(x = times[:,0], y = times[:,1])
plt.show
    
print(prime_numbers(a))