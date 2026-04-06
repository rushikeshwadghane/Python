def findTwoElement(arr):
    res = []
    find  =  {}
    n = len(arr)
    for i in range(n):
        ca =  find.get(arr[i],0)
        find[arr[i]] = ca + 1
        c = find[arr[i]]
        if c > 1:
            res.append(arr[i])
            break
    k = sum(arr) - res[0]  
    m = (( (n ) * (n + 1)) / 2 ) - k
    res.append(int(m))
    return res 


arr  = [1,2,3,5,5]
res = findTwoElement(arr)

print(res)
        
