

try:
    List  =[1,4,5,6]
    print(List[2])
except IndexError as obj:
    print(obj)    
 
except ArithmeticError as eobj:
    print(eobj)
    
else:
    print(List)         
    
finally:
    print("In Finally block")    