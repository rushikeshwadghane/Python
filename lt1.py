def twoSum(nums, target):
    # Create a dictionary to store the number and its index
    seen = {}
    
    for i, num in enumerate(nums):
        # Calculate the complement
        complement = target - num
        print('complement',complement)
        print(seen)
        # Check if the complement exists in the dictionary
        if complement in seen:
            return [seen[complement], i]
        
        # If not, store the number and its index in the dictionary
        seen[num] = i

    # Return an empty list if no solution is found (although the problem guarantees one solution)
    return []

l = [11,22,7,2]
target = 9

res = twoSum(l,target)

print('response',res)