class person:
    'Person hello'
    
    def __init__(self):
        self.name=""
        self.age=""
        self.address=""
    
    
    
    
    def readData(self):
        self.name=str(input("Enter Your Name"))
        self.age=int(input("enter Your Age"))
        self.address=input("Enter Address")
        
    def showData(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Address: ",self.address)
        
    
   
   
    
    
   
    def __del__(self):

        del person
    def __str__(self):
        
        return "Name: "+self.name+"\nAge: "+str(self.age)+"\nAddress: "+self.address
        
if __name__=="__main__":
    p1=person()
    p1.readData()
    #p1.showdata()
    print(p1)
        
        

