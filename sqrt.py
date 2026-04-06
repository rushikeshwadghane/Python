
def mySqrt(x:int):
    low  = 0
    high = x

    while low <= high:
        mid = (low + high) // 2

        if mid * mid == x:
            return mid
        
        elif mid * mid < x:
            ans = mid
            low = mid + 1

        else:
            high = mid  - 1

    return ans

