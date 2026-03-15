
# Write a function to count the number of unique digits in a number -
# eg 111 -> 1
# 121 -> 2
# 123 -> 3

def count_unique_digit(n):
    cnt = 0
    rep = {}
    while n > 0:
        d = n % 10
        rep[d] = rep.get(d,0) + 1
        if rep[d] == 1:
            cnt += 1
        n = n // 10
    return cnt

n = 111
print(len(set(str(n))))
n = 123
# print(len(set(n)))
    
print(count_unique_digit(111))
print(count_unique_digit(121))
print(count_unique_digit(123))
