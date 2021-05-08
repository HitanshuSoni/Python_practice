class AOP:
    def __init__(self):
        self.a=0
        self.b=0
        
    def read(self):
        self.a=int(input("Enter the number"))
        self.b=int(input("Enter the number"))

    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
if __name__=="__main__":

    a1=AOP()
    a1.read()
    print(a1.add())
    print(a1.sub())
    print(a1.mul())
    print(a1.div())
