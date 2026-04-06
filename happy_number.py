def isHappy( n: int,seen= set()) -> bool:
    if n == 1:
        return True
    elif n < 1:
        return False
    if n in seen:
        return False
    num = 0    
    seen.add(n)
    while n > 0:
        r = n % 10
        num += r * r
        n = n // 10

    return isHappy(num,seen)

print(isHappy(10))
