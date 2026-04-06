def findEquilibrium(arr):
    l = len(arr)
    ls = 0
    o = -1
    for i in range(1,l):
        ls += arr[i -1]
        j = i + 1
        rs = 0 
        while j < l:
            rs += arr[j]
            # if rs >= ls:
            #     break
            j += 1
        print(i,j, ls,rs)
        if  ls == rs:
            o = i
            break
        
    return o

r = findEquilibrium([-7, 1, 5, 2, -4, 3, 0])
print(r)

            
        
            


            
            