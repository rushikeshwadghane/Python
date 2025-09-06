
arr = [2,3,4,5,6,7,8,9,10,11,12,13]

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


index = binary_search(arr,8)

print(index)