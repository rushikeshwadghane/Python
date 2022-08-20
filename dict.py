n= int(input("Enter value of n: "))
num = list()
for i in range(n):
    d=int(input())
    num.append(d)
     
data = dict()

for i in range(2,10):
    value = list()
    for j in num:
        if j%i==0:
            value.append(j)
    if(len(value)> 0):
        data.update({i:value})
            
print(data)                 