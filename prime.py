
# def prime(n):
def prime( n):
    if n <= 1:
        return False
    
    for i in range(2, int(n ** 0.5 ) + 1):
        if n % i == 0:
            return False
    return True 
        
# num = int(input("Enter number: "))        
# check = prime(num)
# if check==True:
#     print("Number is prime")
# else:
#     print("not prime")                
        




print(7/2)
print(7//2)
print((8 ** 2))
print(5 ** 2)
    