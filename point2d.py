class point2d:

    def __init__(self):
        self.x=0
        self.y=0

    def read_point(self):
        self.x=int(input("Enter the first Point"))
        self.y=int(input("Enter the second Point"))

    def __str__(self):

        return "coordinates x and y is:"+str(self.x)+","+str(self.y)


if __name__=="__main__":
    
    p1=point2d()
    p1.read_point()
    print(p1)


