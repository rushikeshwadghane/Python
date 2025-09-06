class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        h = len(arr) -1
        l = 0
        while l <= h:
            mid = (l+h)//2
            if arr[mid] == k:
                return mid
            elif arr[mid] > k:
                h = mid -1  
            else:   
                l= mid + 1
        return -1
        
    
class_obj = Solution()
result = class_obj.binarysearch([1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5], 3)
print(result)