"""Finds pairs of values that add up to a target."""


arr = [2,3,5,7,2,5,7,6,9,11,12,5,7,9,1,-1,-2]
target  =  10
#proble statement -  find index of pair which element sum = traget
n  = len(arr)
result  = []
seen  = {}

for i in range(n):
    c = target - arr[i]
    s = seen.get(c,None)
    if s:
        result.append([c,arr[i]])
        seen[c] = False

    if s is None:
        seen[arr[i]] = True


print(result)
