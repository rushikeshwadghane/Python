

arr = [1,-1,-2,3,4,5,-6,6,-7]
nl  = []
nx = []
for i in arr:
    if i < 0:
        nl.append(i)
    else:
        nx.append(i)

print(nl+nx)
    