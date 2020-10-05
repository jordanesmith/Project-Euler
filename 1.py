list_1 = []
for i in range(1000):
    if i%3 == 0:
        list_1.append(i)
    elif i%5 == 0:
        list_1.append(i)

#print(len(list_1))

sum_1 = 0

for i in list_1:
    sum_1 += i

print(sum_1) 
  
