

def kth_smallest(k:int,arr:list):
    l = len(arr)
    i = 0
    if k > l:
        return 0
    for i in range(l):
        for j in range(0,l-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1] , arr[j] = arr[j],arr[j+1]
    sm =  arr[k-1]
    return sm

def kth_smallest_using_sort(k:int,arr:list):
    l = len(arr)
    if l <= 1:
        return arr
    
    mid = l//2
    i = j = 0
    sor_a = []
    left = kth_smallest_using_sort(4,arr[:mid])
    right = kth_smallest_using_sort(4,arr[:mid])
    print(left)
    print(right)
    while i < len(left) and j < len(right):
        print(left[i],right[j],i,j)
        if left[i] <= right[j]:  
            sor_a.append(left[i])
            i+= 1
        else:
            sor_a.append(right[j])
            j+= 1
        print(sor_a)
    print(left[i:],right[j:])
    sor_a.extend(left[i:])
    sor_a.extend(right[j:])
    print(sor_a)
    return sor_a


arr =  [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4

# res = kth_smallest(k,arr)
res1 = kth_smallest_using_sort(k,arr)
# print('k smallest',res)
print('k smallest',res1)