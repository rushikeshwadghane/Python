

def longest_substring(s:str):
    if not s or s == "":
        return 
    l = len(s)
    ml = 1
    for i in range(l):  
        seen = {}     
        seen[s[i]] = seen.get(s[i],0) + 1
        ss = s[i]
        for j in range(i+1,l):
            seen[s[j]] = seen.get(s[j],0) + 1
            if seen[s[j]] <= 1:
                ss += s[j]
            else:
                break   
            if len(ss) > ml:
                ml = len(ss)
    return ml
        
res = longest_substring("pwwkew")
print(f"final result: {res}")
    
