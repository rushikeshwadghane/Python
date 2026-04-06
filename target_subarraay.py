
def sub_array_with_sum(arr,target):
    cs = 0
    st = 0
    for end in range(len(arr)):
        cs += arr[end]
        while cs > target and st <= end:
            cs -= arr[st]
            st += 1
        if cs == target:
            return [st + 1,end +1]
    return [-1]
arr = [1, 2, 3, 7, 5]
target = 12
r = sub_array_with_sum(arr,target)
print(r)


