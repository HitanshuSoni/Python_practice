class country:
    def __init__(self):
        self.name="India"
        self.capital="Delhi"
        self.PM="Mr.Narender Modi"
    def readData(self):
        self.name=str(input("Enter Country Name:"))
        self.capital=str(input("Enter capital Name of Country:"))
        self.PM=str(input("Enter the P.M Name"))
    def showData(self):
        print("Country Name is:",self.name)
        print("Capital of country", self.capital)
        print("P.M Name :",self.PM)
    def __str__(self):
        return "Country Name is:"+self.name+"\n"+"Capital of country: "+self.capital+"\n"+"P.M Name :"+self.PM+"\n"
    def __del__(self):
        del country
if __name__=="__main__":

    c1=country()
    c1.readData()
    #c1.showData()
    print(c1)
        
