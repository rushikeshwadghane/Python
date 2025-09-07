
def find_second_max(arr =[]):

    max  = int()
    s_max = int()
    print(s_max)
    for i in range(0,len(arr)):
        if arr[i] > max:
            s_max = max
            max = arr[i]
        if max > arr[i] > s_max:
            s_max = arr[i]
        
    return s_max


a =  [12, 35, 1, 10, 34, 1]
res = find_second_max(a)

print('********>>',res)