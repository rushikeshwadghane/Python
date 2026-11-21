"""Practice example covering map filter reduce."""


arr = [1,2,3,4,5,6,7,8]

[x for x in range()]

res = list(map(lambda x:x*2,arr))
print(res)

res = list(filter(lambda x : x%2 == 0,arr))
print(res)

from functools import reduce
res =  (reduce(lambda a,b : a+b, arr ))

print(res)


add = lambda a : a + 5
print(add(10))

nums  = [x for x in range(1,11)]
res = map(lambda a : a * 2 , nums)
print(list(res))

r = filter(lambda b : b % 2 == 0 ,nums)
print(list(r))

from functools import reduce
l = reduce(lambda a,b : a + b ,nums)
print(l)
