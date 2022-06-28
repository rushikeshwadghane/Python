class demo:
    
    def __init__(self):
        print("Hello")
    
    def Display(self):
        print("python")
    def __del__(self):
        print("Inside Destructor")
        

obj = demo()

obj.Display()        


