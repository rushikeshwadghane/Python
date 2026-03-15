
def rev_arr(l,r,arr):
    if l >= r:
        return arr
    
    arr[l],arr[r] = arr[r],arr[l]

    return rev_arr(l+1,r-1,arr)
    
arr = [2,4,1,3,5,7,8]

print(rev_arr(0,len(arr)-1,arr))