def findFloor(arr, x):
    mid = len(arr)//2
    o = -1

    print(mid)
    if arr[mid] > x:
        i = mid
        while i >= 0:
            if arr[i] <= x:
                o = i
                break
                    
            i -= 1
    
    if arr[mid] <= x:
        j = len(arr) -1
        while j >= mid:
            print(j)
            if arr[j] <= x:
                o = j
                break
            j -= 1
    if arr[mid] == x:
        o = mid
    return o


r = findFloor([1, 2, 8, 10, 10, 12, 19],11)
print(r)