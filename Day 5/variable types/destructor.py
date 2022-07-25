class A:  
    
    #  we will initialize the class  
    def __init__(self):  
        print(' The class called A is CREATED.')  
class B:  
    def __init__(self, c):  
        self.c = c  
class C:  
    def __init__(self):  
        self.b = B(self)  
    def __del__(self):  
        print("C is deleted")  
def function():  
    c = C()  
    
function()  