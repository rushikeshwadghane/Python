arr = [1,2,4,5,6,7,8,9,10]

def binary_search(arr:list,n):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l+r) //2
        while (m - 1) >= l and arr[m - 1] == n:
            m -= 1            
        if arr[m] == n:
            return m
        if arr[m] > n:
            r = m - 1
        else:
            l  = m +1

    return - 1

def binary_search(arr,k):
    l  = 0
    r = (len(arr)- 1)
    while l < r:
        mid = (l+r) // 2
        if arr[mid] == k:
            while (mid - 1) >= l and arr[mid-1] == k:
                mid -= 1
            return mid
        elif arr[mid] < k:
            l = mid + 1
        else:
            r = mid + 1
    return -1

arr = [1 ,1, 1, 2, 2 ,3, 3, 3 ,3, 3, 3, 4, 4 ,4 ,5, 5, 5]
r = binary_search(arr,3)
print(r)