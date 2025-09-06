def findDuplicates(arr):
    freq = {}
    result = []
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    for k, v in freq.items():
        if v == 2:
            result.append(k)
    return result



res = findDuplicates([5, 15, 2, 7, 8, 2, 3, 1])
print(res)