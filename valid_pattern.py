

def wordPattern(pattern: str, s: str) -> bool:
    s = s.split()
    if len(pattern) != len(s):

        return False
    hash2 = {}
    j = -1
    p1 = ""
    for i in pattern:
        v = hash2.get(i,None)
        if not v:
            j += 1
            hash2[i]  = j
            p1 += str(j)
        else:
            p1 += str(v)
    hash1 = {}
    p2 = ""
    n = -1
    for k in s:
        v = hash1.get(k,None)
        if not v:
            n += 1
            hash1[k]  = n
            p2 += str(n)
        else:
            p2 += str(v)
    print(p1,'-----',p2)
    return p1 == p2


print(wordPattern('abba',"dog cat cat fish"))