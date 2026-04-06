def merge_sort(arr):
    if len(arr) <= 1:
        return arr          # MUST return a list
    
    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    i = j = 0
    result = []
    print(left,'-------------')
    print(right,'============')
    while i < len(left) and j < len(right):
        print(left[i],right[j],i,j)
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    print(result,'rr')
    result.extend(left[i:])
    result.extend(right[j:])
    return result



arr =  [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
res =  merge_sort(arr)
print(res)