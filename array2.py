
arr = [2,3,5,7,2,5,7,6,9,11,12,5,7,9,1,-1,-2]
target  =  10

#proble statement -  finde index of pair which element sum = traget

n  = len(arr)
result  = []

for i in range(n):
    for j in range(i+1, n):

        if arr[i] + arr[j] == target:
            if arr[i] > arr[j]:
                pair =  [arr[j],arr[i]]
            else:
                pair =  [arr[i],arr[j]]

            dup = False

            for p in result:
                if p[0] == pair[0] and p[1] == pair[1]:
                    dup = True
                    break
            if not dup:
                result.append(pair)

print(result)