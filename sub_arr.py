#kadanes algo
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
arr  = [1, 2, 4, -2, 5]

current_sum  = arr[0]
max_sum = arr[0]

for i in range(1, len(arr)):
    # current_sum = max(arr[i], current_sum + arr[i])
    if current_sum + arr[i] > arr[i]:
        current_sum = current_sum + arr[i]
    else:
        current_sum = arr[i]

    # max_sum = max(max_sum, current_sum)
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)

