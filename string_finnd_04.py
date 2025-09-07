n,m = map(int,(input().split()))

nl = []
for s in range(n):
    nv = input()
    nl.append(nv)

for i in range(m):
    l = []
    mv = input()
    for ind,j in enumerate(nl):
        if mv == j:
            k = ind +1
            l.append(k)
    if not l:
        l = [-1]
    print(*l)

