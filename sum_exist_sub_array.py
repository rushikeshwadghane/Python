def twoSum(arr, target):
    l = len(arr)
    seen = []
    for i in range(l):
        com = target - arr[i]
        if target == 0 and arr[i] == 0:
            continue
        if com in seen :
            return True
    
        seen.append(arr[i])
    return False


target = -17
# arr = [1, -2, 1, 0, 5]
# arr = [0, -1, 2, -3, 1]
arr = [-4, -3, 2, -5, -10, -7]
print(twoSum(arr, target))