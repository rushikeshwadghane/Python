def three_sum(arr: list, target: int) -> list:
    res = []
    n = len(arr)
    
    arr.sort()

    for i in range(n - 2):

        # skip duplicate fixed elements
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        l = i + 1
        r = n - 1

        while l < r:
            total = arr[i] + arr[l] + arr[r]

            if total == target:
                res.append([arr[i], arr[l], arr[r]])

                l += 1
                r -= 1

                # skip duplicates for left pointer
                while l < r and arr[l] == arr[l - 1]:
                    l += 1

                # skip duplicates for right pointer
                while l < r and arr[r] == arr[r + 1]:
                    r -= 1

            elif total < target:
                l += 1
            else:
                r -= 1

    return res


nums = [-1,0,1,2,-1,-4]
k = 0

print(three_sum(nums, k))
nums = [-1,0,1,2,-1,-4]
k = 0
r = three_sum(nums,k)

print(r)


