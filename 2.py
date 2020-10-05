def fib(a):
    if a <= 0:
        raise Exception("Number not in range")
    if a > 1:
        b = [1, 2]
    
        for i in range(a-2):
            term = b[i] + b[i+1] 
            b.append(term)
    
        return(b)
    else:
        return([1])

sum_1 = 0
i = 1
while fib(i)[-1] <= 4e6:
        
    if fib(i)[-1]%2 == 0:
        sum_1 += fib(i)[-1]
    
    i += 1
print(sum_1)
print(fib(35))