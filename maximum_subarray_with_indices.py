"""Finds a maximum-sum subarray and tracks its start and end indices."""


# Modified Kadane
# 4. Longest Subarray With Maximum Sum
# Time Complexity: O(n)
# Space Complexity: O(1)

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# arr  = [1, 2, 4, -2, 5]


current_sum  = arr[0]
max_sum = arr[0]

start = 0
end = 0
temp = 0


for i in range(1,len(arr)):

    if arr[i] > current_sum  + arr[i]:
        current_sum = arr[i]
        temp = i
    else:
        current_sum += arr[i]

    if current_sum > max_sum:
        max_sum = current_sum
        start = temp
        end = i


print(max_sum)
print(arr[start:end+1])
