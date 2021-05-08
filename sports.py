class sports:
    def __init__(self):
        self.name=""
        self.type=""

    def readData(self):
        self.name=str(input("Enter SPORT Name"))
        self.type=str(input("Enter Sport Type"))

    def showData(self):
        print("Sport Name:",self.name)
        print("Sport Type:",self.type)

    def __del__(self):

        del sports
    def __str__(self):

        return "Sport Name: "+self.name+"\n"+"Sport Type: "+self.type
if __name__=="__main__":
    s1=sports()
    s1.readData()
    #s1.showData()
    print(s1)
    

    
        
