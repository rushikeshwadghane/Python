

def long_even_word(s):
    l = s.split(" ")
    ml = 0
    for i in l:
        n = len(i)
        if n%2 == 0:
            ml = max(ml,n)
    return ml


print(set('gfsdfkdsn'))
