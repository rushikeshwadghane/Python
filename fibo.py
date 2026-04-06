
# 0 1 1 2 3 5 8 13
# 0 1 2 3 4 5 6 7

def nth_fibo_number(n):
    if n <= 1:
        return n
    n1,n2 =0,1
    for _ in range(2,n+1):
        n1,n2 = n2, n1+n2
    return n2

def fibo(n,memo = {}):
    if n <= 1:
        return n
    print(memo)
    if n not in memo:
        memo[n]  = fibo(n-1) + fibo(n-2)
    return memo[n]



def n_fibo(n,a= 0,b = 1):
    res = [0,1]
    while n > 1:
        a,b = b , a + b
        res.append(b)
        n -= 1
        n_fibo(n,a,b) 
    return res


print(n_fibo(5))
# 0 1 1 2 3 5 
