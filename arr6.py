def find_duplicates(arr):
    # arr.sort()
    duplicates = []
    n = len(arr)
    
    for i in range(1, n):
        print(arr[i], arr[i-1])
        if arr[i] == arr[i-1]:
            if not duplicates or duplicates[-1] != arr[i]:
                duplicates.append(arr[i])
    
    return duplicates


# Example
arr = [2, 2,3, 2, 1, 4, 5, 3, 4, 2, 1, 4]
print(find_duplicates(arr))  # Output: [1, 2, 3, 4]
