

def find_dup_char(s:str):
    n = len(s)
    count = {}
    dup_char = []
    for i in range(n):
        c = count.get(s[i],0) + 1
        if c == 2:
            dup_char.append(s[i])
        count[s[i]] = c

    return dup_char

s = find_dup_char('sdcjdaosdkao')
print(s)