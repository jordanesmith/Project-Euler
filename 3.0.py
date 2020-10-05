'''project euler'''
'''The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?'''

def prime_factors(a):
    factor_list = []
    counter = 2
    while counter <= a:
        if a%counter == 0:
            factor_list.append(counter)
            a /= counter
        elif a%counter != 0:
            counter +=1       
    
    return(factor_list)


