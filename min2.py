arr =  [3,4,5,6,7,7,8,3,4,1,4,7]
arr =  [5,4,5,6,7,7,8,3,4,1,3,4]

f_min = None
s_min = None
f_min_inde = 0
s_min_index = 0

for i in range(len(arr)-1):
    if f_min == None or arr[i] < f_min:
        s_min = f_min
        f_min = arr[i]

    elif  f_min != s_min and  (s_min == None or  arr[i] < s_min < f_min ):
          s_min = arr[i]
    
    min_spend = 0
    if f_min and s_min:
        min_spend = min((f_min + s_min),(arr[i] + (arr[i+1]/2)))

print(min_spend)

