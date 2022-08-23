
def prime(n):
    for i in range(2,n/2+1):
        if n%i==0:
            return False
        else:
            return True
        
num = int(input("Enter number: "))        
check = prime(num)
if check==True:
    print("Number is prime")
else:
    print("not prime")                
        
    