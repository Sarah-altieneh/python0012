class A(object):
    def __init__(self,a):
        self.a='a'
        print(self.a)
    def hi (self):
        print('hi from A')      
class B(object):
    def __init__(self,b):
        self.b='b'
        print(self.b)
    def hi (self):
        print('hi from B')    
class C(A,B):
    def __init__(self,a,b):
        self.c='c'
        print(self.c)
        A.__init__(self,a)
        B.__init__(self,b)
o=C('x','z')
print("#"*20)
o.hi()        
