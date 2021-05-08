class academic:
     def __init__(self):
        self.roll=""
        self.per=""

     def readData(self):
        self.roll=int(input("Enter  Roll No."))
        self.per=float(input("Enter Percentage"))

     def showData(self):
        print("Roll No.: ",self.roll)
        print("Percentage: ",self.per,"%")

     def __del__(self):

        del academic
     def __str__(self):

        return "Roll no.: "+str(self.roll)+"\n"+"Percentage: "+str(self.per)+"%"
if __name__=="__main__":
    a1=academic()
    a1.readData()
    #a1.showData()
    print(a1)
