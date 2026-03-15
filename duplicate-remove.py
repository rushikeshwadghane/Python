arr = [2,3,2,1,4,5,3,4,2,1,4]
new = []
dup = {}

for i in arr:
    dup[i] = dup.get(i,0) + 1
    if dup[i] <= 1:
        j = 0
        while j < len(new) and new[j] < i:
            j+= 1
        new.insert(j,i)
print(new)
print(dup)


