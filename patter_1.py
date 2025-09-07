
n = int(input('Please enter value of n it should be odd number '))
m = int(n * 3)
for i in range(n//2):
    j = int((2*i) + 1)  
    print(('.|.' * j).center(m,'-'))
print(('WELCOME').center(m,'-'))

for k in range(n//2,0,-1):
    j = int((2*k) - 1)  
    print(('.|.' * j).center(m,'-'))
