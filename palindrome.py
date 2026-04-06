
from functools import reduce

def pal(s):
    return s == s[::-1]

def reverse_string(s):
    j = len(s) -1
    i = 0
    nl = list(s)
    while i < j:
        i += 1
        j -= 1
    ns = "".join(nl)
    print(ns)
    return s == ns

def rev_str_rec(s,i,j):
    if i > j:
        return s
    else:
        nl = list(s)
        nl[i],nl[j] = nl[j],nl[i] 
        i += 1
        j -= 1
        ns = "".join(nl)
        s = rev_str_rec(ns,i,j)
        return s

# print(pal('madam'))
# print(reverse_string('abc'))
s = "abc"
print(rev_str_rec(s,0,len(s)-1))

