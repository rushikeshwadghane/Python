class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0 
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                print(nums)
                k += 1
        return k


# Example usage:
solution = Solution()
nums = [3,2,2,3]
val = 3
result = solution.removeElement(nums, val)
print(result)  # Output the new length after removal