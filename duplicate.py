"""Practice example defining or demonstrating `findDuplicates`."""

def findDuplicates(arr):
    arr.sort()
    l = 0
    for r in range(1,len(arr)):
        if arr[l] != arr[r]:
            l += 1
            arr[l] =  arr[r]
    arr[:] = arr[:l+1]
    return arr

res = findDuplicates([5, 15, 2, 7, 8, 2,1,5, 3, 1,5,5])
print(res)
