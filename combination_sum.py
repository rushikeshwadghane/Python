from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    res = []

    def backtrack(start, path, remaining):
        print('start',start,'path',path,'remaining',remaining)
        if remaining == 0:
            res.append(path[:])
            return
        
        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])  
            path.pop()

    backtrack(0, [], target)
    return res


candidates = [2,3,5]
target = 8
print(combinationSum(candidates, target))