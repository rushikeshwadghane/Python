arr1 =  [3, 4, 5, 2]
arr2  = [-10, -20, 1, 2]
arr3 =  [1, 5, -10, -20]



def max_product(nums: list[int]) -> int:
    # Step 1: Initialize variables
    max1 = max2 = float('-inf')  # Two largest numbers
    min1 = min2 = float('inf')   # Two smallest numbers

    # Step 2: Find max1, max2, min1, min2 in a single pass through the array
    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
        
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    # Step 3: Calculate the two possible products and return the maximum
    product1 = max1 * max2
    product2 = min1 * min2
    return product1,product2



mp ,np = max_product(arr1)
print('max product',mp,'min product',np)
mp ,np = max_product(arr2)
print('max product',mp,'min product',np)
mp ,np = max_product(arr3)
print('max product',mp,'min product',np)


