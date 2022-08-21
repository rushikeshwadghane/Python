data  = [8,3,45,45,23,12,9,18,24,45,76]
print(data)
data.append(5)

print(data)
data.insert(0,17)   #to  add element at specific positon

print(data)

data.pop()
print(data)

s= data.pop(4)
print(s)
print(data)

# data.reverse()
# print(data)
val = [5,10,25,12,18]
data.extend(val)   #add list to existing list 
print(data)

data.sort()
print(data)
