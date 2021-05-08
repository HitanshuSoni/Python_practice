from state import state
class district(state):
    def __init__(self):
        state.__init__(self)
        self.name="None"
    def readData(self):
        state.readData(self)
        self.name=str(input("Enter District Name:"))
    def showData(self):
        state.showData(self)
        print("District Name is :",self.name)
    def __str__(self):
        return super().__str__()+"District name is: "+self.name
    def __del__(self):
        del district
if __name__=="__main__":
    d1=district()
    d1.readData()
    #d1.showData()
    print(d1)

        
