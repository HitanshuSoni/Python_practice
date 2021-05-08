class Vector:
   # __slots__=['a','b']
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return 'Vector (%d,%d)'%(self.a,self.b)
    def __add__(self,other):
        return Vector(self.a+other.a,self.b+other.b)
    def __pow__(self,other):
        return Vector(self.a**other.a,self.b**other.b)
    def __mod__(self,other):
        return Vector(self.a%other.a,self.b%other.b)
    def __floordiv__(self,other):
        return Vector(self.a//other.a,self.b//other.b)
    def __lshift__(self,other):
        return Vector(self.a<<other.a,self.b<<other.b)
    def __rshift__(self,other):
        return Vector(self.a>>other.a,self.b>>other.b)
    def __xor__(self,other):
        return Vector(self.a^other.a,self.b^other.b)
v1=Vector(2,10)
v2=Vector(5,-2)
v3=Vector(2,2)
print(v1+v2)
print(v1**v3)
print(v1%v3)
print(v1//v3)
print(v1<<v3)
print(v1>>v3)
print(v1^v3)
v1.c=99
