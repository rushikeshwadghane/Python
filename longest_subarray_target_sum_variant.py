"""Demonstrates finding a longest subarray with a target sum."""


# Q Find longest subarray with sum = k



# arr = [10, 5, 2, 7, 1, -10]
# k = 15
arr =[-5, 8, -14, 2, 4, 12]
k =  -5
# arr = [94, -33, -13, 40 ,-82 ,94, -33, -13, 40, -82]
# k = 52
# arr = [10, 5, 2, 7, 1, -10, -5]
# k = 14
curr_sum = 0
max_len = 0
map_sum = {}

for i in range(len(arr)):
    curr_sum += arr[i]
    if curr_sum == k:
        max_len = i + 1

    check = curr_sum - k

    if check in map_sum:
        max_len = max(max_len, i - map_sum[check])

    if curr_sum not in map_sum:
        map_sum[curr_sum] = i

print(max_len)


curr_sum = 0
map_sum = {}
max_len = 0

for i in range(len(arr)):
    curr_sum += arr[i]
    if curr_sum == k:
        max_len = i + i

    check = curr_sum - k
    if check in map_sum:
        max_len = max(max_len, i - map_sum[check])

    if curr_sum not in map_sum:
        map_sum[curr_sum] = i


print(max_len)
