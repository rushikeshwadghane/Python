arr =  [5,4,8,6,3,1,9,99,-9,8,7,6,12,16,76,78,43,0,2,85]

# [1,3,4,5,6,8,9]

n = len(arr)

for i in range(n):
    for j in range(0,n-i-1):
        if arr[j] < arr[j+1]:
            arr[j],arr[j+1]  = arr[j+1], arr[j]

print(arr)