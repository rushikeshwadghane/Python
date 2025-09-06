
arr = [-1,-2]

max   = -10**9
max2 = 10**-9


for n in arr:
    if n > max:
        max2 = max
        max = n
    
    elif n > max2:
        max2 = n

print(max,max2)