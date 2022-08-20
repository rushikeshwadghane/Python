from distutils.errors import LibError
from typing import List


List1 = [1,2,3,21,4,4,5,6,6,7,7,8,9,1,3]

for i in range(len(List1)):
    flag= 0
    for j in range(i,len(List1)):
        if List1[i]==List1[j] and i!=j:
            flag = 1
    
    if(flag==0):
        print(List1[i])
        
        
print(set(List1))

