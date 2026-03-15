
def f(n,sum):
    print(sum)
    if n < 1:
        return sum
    return f(n-1,sum + n)
print(f(5,0))