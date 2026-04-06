from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    for i in range(len(strs[0])):
        c = strs[0][i]
        for j in range(1,len(strs)):
            if i >= len(strs[j]) or c != strs[j][i]:
                return strs[0][:i]
        
    return strs[0]

        

r =  longestCommonPrefix(["flower","flower","flower"])
print(r)


