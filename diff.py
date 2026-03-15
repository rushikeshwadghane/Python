# Given a List of n integers and a number k, find the pairs of numbers in the list such
# that the difference between the pair is k. Find the optimal solution with and
# without extra storage.

def diff_with_k(arr,k):

    hash = {}
    res  = []
    for i in arr:
        b = i - k
        a = hash.get(i,None)
        if a:
            res.append([a,i])
            i = None
        hash[b] = i

    return res



# arr = [1, 5, 3, 4, 2]
# k = 2
# arr = [8, 12, 16, 4, 0, 20]
# k = 4
# arr = [10, 15, 3, 7]
# k = 5
arr = [1, 1, 1, 2, 2]
k = 0
arr = [5]
k = 3

print(diff_with_k(arr,k))

