def findDuplicates(arr):
    freq = {}
    result = []
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

        if freq[num] == 2:
            result.append(num)

    return result



res = findDuplicates([5, 15, 2, 7, 8, 2,1,5, 3, 1,5,5])
print(res)