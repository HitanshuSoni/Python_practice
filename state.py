from country import country
class state(country):
    def __init__(self):
        country.__init__(self)
        self.name="None"
        self.capital="None"
        self.CM="None"
    def readData(self):
        country.readData(self)
        self.name=str(input("Enter State Name:"))
        self.capital=str(input("Enter capital Name of State:"))
        self.CM=str(input("Enter the C.M Name"))
    def showData(self):
        country.showData(self)
        print("Country Name is:",self.name)
        print("Capital of country", self.capital)
        print("C.M Name :",self.CM)
    def __str__(self):
        return super().__str__()+"State Name is:"+self.name+"\n"+"Capital of State: "+self.capital+"\n"+"C.M Name :"+self.CM+"\n"
    def __del__(self):
        del state
if __name__=="__main__":

    s1=state()
    s1.readData()
    #s1.showData()
    print(s1)
        
