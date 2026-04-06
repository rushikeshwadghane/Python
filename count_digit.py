
def count_digit(n):
    c = 0
    t = n
    while t > 0:
        r = t %10
        # if n % r == 0:
        c+= 1
        t = t // 10

    return c


print(count_digit(121))