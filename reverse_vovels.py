def reverseVowels(s: str) -> str:
    vo =  tuple(['A','a','e','E','I','i','O','o','U','u'])
    l = 0
    s = list(s)
    r = len(s) - 1
   
    while l < r:
        if s[r] not in vo:
            r -= 1
        if  s[l] not in vo:
            l += 1

        if s[l] in vo and s[r] in vo:
            s[l],s[r] = s[r],s[l]
            l += 1
            r -= 1
    return "".join(s)



print(reverseVowels('IceCreAm'))