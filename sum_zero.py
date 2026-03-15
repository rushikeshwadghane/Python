def getPairs(arr):
    res = set()
    seen = set()
    for num in arr:
        print(seen,'---------',num)
        if -num in seen:
            pair = (min(num, -num), max(num, -num))
            res.add(pair)
        seen.add(num)
    
    return sorted(list(res))



arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
res = getPairs(arr)
print(res)