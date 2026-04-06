

def find_pair_of_target(arr:list,target:int):
    
    if not arr or not target:
        return False
    
    left  = 0
    right = len(arr)  - 1

    while left  < right:
        cs = arr[left] + arr[right]

        if cs == target:
            return True
        
        if cs < target:
            left+= 1

        else:
            right -= 1
    return False


arr = [1, 2, 4, 6, 10]


res = find_pair_of_target(arr,8)

print(res)



        

