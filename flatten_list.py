arr = [1,2,3,[3,5,[5,6]],6,7,[9]]

def flatten_list(arr:list):
    res =[]
    for i in arr:
        if isinstance(i,list):
            res.extend(flatten_list(i))
        else:
            res.append(i)
    return res

print(flatten_list(arr))


