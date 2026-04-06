
def check_anagram(str1,str2):

    if len(str1) != len(str2):
        return False
    
    str1 = str1.lower()
    str2 = str2.lower()


    count  = [0] * 26

    for i in str1:
        count[ord(i) - ord('a')] += 1

    for j in str2:
        count[ord(j) - ord('a')] -= 1

    for n in count:
        if n != 0:
            return False
            
    return True


def check_ana(str1,str2):
        if len(str1) != len(str2):
            return False
        
        str1 = str1.lower()
        str2 = str2.lower()

        ns1   = "".join(sorted(str1))
        ns2   = "".join(sorted(str2))
        
        return ns1 == ns2

# Example Usage
print(check_anagram("Listen", "Silent"))  # True
print(check_anagram("Hello", "World"))

print('==================')
print(check_ana("Listen", "Silent"))  # True
print(check_ana("Hello", "World"))  
