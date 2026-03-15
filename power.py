def isPowerofTwo(n):
    if n == 1:
        return True
    for i in range(int(n//2) + 1):
        p = 2 ** i

        print(i,'------------',p)
        if p > n:
            return False
        if p == n:
            return True
    return False


print(isPowerofTwo(4))