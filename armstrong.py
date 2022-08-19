

def CalculatePower(x,y):
    power = 1
    for i in range(1,y+1):
        power = power*x
    print(power)
    return power

def Armstrong(n):
    temp= n
    temp2 = n
    cnt = 0
    while(temp!=0):
        temp = temp/10
        cnt += 1
    
    Sum = 0
    while(n!=0):
        digit = n%10
        power = CalculatePower(digit,cnt)
        n = n/10
        Sum = Sum+power  
        
    if(Sum == temp2):
        return True
    else:
        return False          
 
print("Enter Value")
x =int(input())
ret =  Armstrong(x)
if(ret==True):
    print("No is Armstrong")
else:
    print("not Armstrong")        