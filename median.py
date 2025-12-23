def median(arr1, arr2):
    new_arr = arr1 + arr2
    new_arr.sort()
    l = len(new_arr)

    if l % 2 == 1:   # odd
        return new_arr[l//2]
    else:            # even
        return (new_arr[l//2] + new_arr[l//2 - 1]) / 2




arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(median(arr1, arr2))