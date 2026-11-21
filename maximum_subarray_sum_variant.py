"""Demonstrates an alternative implementation of maximum subarray sum."""


# 1. Kadane's Algorithm — Maximum Subarray Sum
# Find maximum sum of contiguous subarray

# Time Complexity: O(n)
# Space Complexity: O(1)

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
arr  = [1, 2, 4, -2, 5]


current_sum  = arr[0]
max_sum = arr[0]

for i in range(1, len(arr)):
    if current_sum + arr[i] > arr[i]:
        current_sum = current_sum + arr[i]
    else:
        current_sum = arr[i]

    max_sum = max(max_sum, current_sum)

print(max_sum)
