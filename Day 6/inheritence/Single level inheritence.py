class A(): #its a parent class or super class
   def f1(self):
    print('A')
class B(A): # its a child class
   def f2(self):
     print('B')
ob=B()
ob.f1()
ob.f2()