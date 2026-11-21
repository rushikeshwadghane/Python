"""Uses a sliding window to find a contiguous subarray with a target sum."""

#User function Template for python3
# 4. Subarray With Given Sum (Sliding Window)
# Find subarray with given sum

# Sliding Window

# BUT ONLY WORKS WHEN
# Array contains positive numbers

class Solution:
    def subarraySum(self,arr, target):
        left = 0
        curr = 0

        for right in range(len(arr)):
            curr += arr[right]

            while curr > target:
                curr -= arr[left]
                left += 1

            if curr == target:
                return [left+1, right+1]

        return -1


obj = Solution()

res = obj.subarraySum([1,2,3,7,5], 12)
# res = obj.subarraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)

print(res)
