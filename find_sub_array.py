def find_subarray_with_sum(arr, target):
    start = 0
    curr_sum = 0

    for end in range(len(arr)):
        curr_sum += arr[end]
        print(start,'start1',end,curr_sum)
        # Shrink window from the left if needed
        while curr_sum > target and start <= end:
            curr_sum -= arr[start]
            start += 1
            print(start,'start1')
        
        print(start,'start3')


        if curr_sum == target:
            return [start + 1, end + 1]  # 1-based index

    return [-1]



arr = [1, 2, 3, 7, 5]
target = 12

res = find_subarray_with_sum(arr,target)

print('result -------->',res)
