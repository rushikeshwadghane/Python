

def convert_name(name):
    l = name.split(' ')
    print(l)
    nl  = []
    for i in l:
        print(i)
        if i:
            n= chr(ord(i[0])-32)
            nt = i[:0] + n + i[1:]
            nl.append(nt)
    
    return " ".join(nl)
        
        
        

s = str(input())

c = convert_name(s)

print(s)
print(c)

