from functools import reduce


list1 = [1,2,3,4,5,6,7,8,9,10]

# def additon(x,y):
#     ans = x+y
#     return ans

# sum1 = reduce(additon,list1)

# print(sum1)

sum1 = reduce(lambda x,y:x+y,list1)
print(sum1)