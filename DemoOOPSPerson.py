class person:
    'Person hello'
    count=0
    
    
    
    
    def getinfo(self):
        self.name=str(input("Enter Your Name"))
        self.age=int(input("enter Your Age"))
        self.address=input("Enter Address")
    def putinfo(self):
        print("Name:",getattr(self,'name',None),"Age:",getattr(self,'age',0),"Address:",getattr(self,'address',None))
    '''def __init__(self):
        self.name=""
        self.age=""
        self.address=""'''
    '''def __init__(self,name,age,address):
         self.name=""
         self.age=""
         self.address=""'''
    #init is constructor
    
    #paramerter construtor
    def __init__(self,name=None,age=0,address=None):
         self.name=name
         self.age=age
         self.address=address
         person.count+=1
    def personCount(self):
        print("Persons are",person.count)
        #del distructor
    def __del__(self):
        print("Destructor")
        person.count-=1
    def __str__(self):
        
        return "Name= "+self.name+"\nAge= "+str(self.age)+"\nAddress= "+self.address
        
        
        
        
P1=person()
P2=person("Hitu",20,"76 VB")
P2.putinfo()
P1.getinfo()
P1.putinfo()
person.personCount(person.count)
del(P2)
print("yha P1 Ka name delete hoyega Ab")
del P1.name#del a perticula atribute  #delattr(P2,'name')
print(hasattr(P1,"name"))
P1.putinfo()

person.personCount(person.count)
print("Yha P1 ka name vapis aayega ")
setattr(P1,"name","Shivuu")
print(P1.name)
print("class name",person.__class__)
print("Dict =",person.__dict__)
print("Dir =",person.__dir__(P1))
print("Doc =",person.__doc__)    
print("Module =",person.__module__)
print("Size of =",P1.__sizeof__())

#call by object
print(P1)

