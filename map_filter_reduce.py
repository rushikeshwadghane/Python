
arr = [1,2,3,4,5,6,7,8]

res = list(map(lambda x:x*2,arr))
print(res)

res = list(filter(lambda x : x%2 == 0,arr))
print(res)

from functools import reduce
res =  (reduce(lambda a,b : a+b, arr ))

print(res)
