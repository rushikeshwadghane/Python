arr = [5,6,3,5,6,7,8,3,5,6,8,2,1,6]

target = 10

pair = []
find = []
for num in arr:
    check = target - num
    if num in find:
        pair.append([check,num])
    find.append(num)

print(pair)