
def searchRange(nums: list[int], target: int) -> list[int]:
    res = [-1,-1]    
    n = len(nums)
    l = 0
    r  = n - 1
    while l <= r:
        if nums[l] == target and res[0] == -1:
            res[0] = l
        
        
        if nums[r] == target and res[1] == -1: 
            res[1] = r
             
        if res[0] == -1:
            l += 1

        if res[1] == -1:
            r -= 1
        if res[0] != -1 and res[1] != -1:
            break

    return res

nums =  [1]
target= 1
print(searchRange(nums,target))

nums = [5,7,7,8,8,10]
target = 8
# Output: [3,4]
# print(searchRange(nums,target))
nums = [5,7,7,8,8,10]
target = 6
# print(searchRange(nums,target))
# Output: [-1,-1]
nums = []
target = 0
# print(searchRange(nums,target))
# Output: [-1,-1]
