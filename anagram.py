from collections import Counter

def check_anagram(str1,str2):

    if len(str1) != len(str2):
        return False
    print(ord(str1[0]))
    str1 =  str1.lower()
    str2 =  str2.lower()
    
    return Counter(str1) == Counter(str2)

print(check_anagram("Listen", "Silent"))  # True
