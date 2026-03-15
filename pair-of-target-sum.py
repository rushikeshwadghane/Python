#proble statement -  finde index of pair which element sum = traget

# def return_pair_of_index(target:int,arr:list):
#     if not arr or not target:
#         print('Check array and target')
#         return
#     result = []

#     l = len(arr)
#     count = 0
#     for i in range(l):
#         for j in range(i+1,l):
#             if arr[i] + arr[j] == target:
#                 if arr[j] > arr[i]:
#                     pair = [arr[j],arr[i]]
#                 else:
#                     pair  = [arr[i],arr[j]]

#                 dup = False
#                 for p in result:
#                     if p[0] == pair[0] and p[1] == pair[1]:
#                         dup = True
#                         break
#                 if not dup and pair:
#                     count+= 1
#                     result.append(pair)
        
#     return result,count

# arr = [2,3,5,7,2,5,7,6,9,11,12,5,7,9,1,-1,-2]
# target  =  10
# res,c = return_pair_of_index(target,arr)
# print(res,c,len(res))


def count_pairs(target,arr):
    freq = {}
    cnt = 0
    l = len(arr)

    for i in range(l):
        comp = target - arr[i]
        print(comp)
        if comp in freq:
            cnt += freq[comp]
        freq[arr[i]] = freq.get(arr[i],0) + 1

    return cnt


arr = [1, 5, 7, -1, 5] 
target = 6 

res = count_pairs(target,arr)

print(res)
