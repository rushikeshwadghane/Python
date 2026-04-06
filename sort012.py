arr =  [0,1,2,0,1,2]


pos = 0
for i in range(len(arr)):
    if arr[i] == 0:
        arr[i],arr[pos] = arr[pos],arr[i]
        pos += 1

for i in range(pos,len(arr)):
    if arr[i] == 1:
        arr[i],arr[pos] = arr[pos],arr[i]
        pos += 1

print(arr)

