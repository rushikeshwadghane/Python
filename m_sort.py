
def merger_sort(arr:list):

    if len(arr) <= 1:
        return arr

    mid  = len(arr)//2
    
    left = merger_sort(arr[mid:])
    right = merger_sort(arr[:mid])
    
    res = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i+= 1
        else:
            res.append(right[j])
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])

    return res


a = [5, 4, 3, 2, 1]
arr = [34, 12, 78, 56, 23, 89, 1]
arr1  = [-3, -5, -1, -4, -2]

print(merger_sort(a))
print(merger_sort(arr))
print(merger_sort(arr1))

