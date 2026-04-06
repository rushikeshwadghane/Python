arr = [10, 5, 2, 7, 1, -10]
k = 15
# arr =[-5, 8, -14, 2, 4, 12]
# k =  -5
# arr = [94, -33, -13, 40 ,-82 ,94, -33, -13, 40, -82]
# k = 52
# arr = [10, 5, 2, 7, 1, -10, -5]
# k = 14
curr_sum = 0
max_len = 0
map_sum = {}

for i in range(len(arr)):
    curr_sum  += arr[i]
    if curr_sum ==  k:
        max_len = max(max_len,i + 1)
    c = curr_sum - k
    prev_ind = map_sum.get(curr_sum - k, None)
    print(prev_ind,i,c)
    if prev_ind is not None:
        max_len = max(max_len, i - prev_ind)
    if curr_sum not in map_sum:
        map_sum[curr_sum] = i  
    print(map_sum)      

print(max_len)

