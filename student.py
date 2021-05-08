from person import person
from sports import sports
from academic import academic

class student(person,sports,academic):

    def __init__(self):
        person.__init__(self)
        sports.__init__(self)
        academic.__init__(self)
    def readData(self):
        
        person.readData(self)
        sports.readData(self)
        academic.readData(self)
    def showData(self):
        person.showData(self)
        sports.showData(self)
        academic.showData(self)
    def __del__(self):

        del student

    def __str__(self):

        return person.__str__(self)+sports.__str__(self)+academic.__str__(self)

if __name__=="__main__":

    st1=student()
    st1.readData()
    #st1.showData()
    print(st1)
    
        
        
        
