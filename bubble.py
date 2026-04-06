arr = [3,4,6,1,2,4,5]

from copy import copy,deepcopy

new_arr = deepcopy(arr)

n =  len(arr)
for i in range(n):
    for j in range(n-1-i):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

print(arr)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    res = []
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

print(merge_sort(new_arr))




