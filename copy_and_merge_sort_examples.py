"""Demonstrates shallow and deep copies and includes a merge-sort example."""


from copy import copy,deepcopy
a = [1,2,[3,4]]
d = [1,2,[3,4]]
b = copy(a)
c = deepcopy(d)

b[0] = 99
b[2][0] = 100
c[2][0] = 100

print(a)
print(b)
print(d)
print(c)





def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    res = []
    i = j  = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res
arr = [3,4,6,1,2,4,5]
print(merge_sort(arr))
