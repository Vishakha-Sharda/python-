class A ():
    def f1(self):
        print('A')
class B(A):
    def f2(self):
        print('B')
class C(B):
    def f3(self):
        print('C')
ob=C()
ob.f1()
ob.f3()