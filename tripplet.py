
def triplet_sum(arr:list,target):
    n = len(arr)
    res = []
    arr.sort()
    for i in range(n):
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left = i + 1
        right = n - 1 

        while left < right:
            total  = arr[i] + arr[left] + arr[right]

            if total == target:
                res.append([arr[i],arr[left],arr[right]])
                
                while left < right and arr[left] == arr[left +1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < target:
                left+= 1
            else:
                right -= 1

    return res


print(triplet_sum([1, 2, -1, 0, -2, 1, -1], 0))


