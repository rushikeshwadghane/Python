arr = [2,3,2,1,4,5,3,4,2,1,4]

# problem statement -  Remove duplicate element from array and sort array asscending order

new  = []

for n in arr:
    if n not in new:
        i = 0
        while i < len(new) and new[i] < n:
            i+= 1
        new.insert(i,n)

print(new)
