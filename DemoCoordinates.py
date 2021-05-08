class point2d:

    def read_point(self):
        self.x=int(input("Enter the first Point"))
        self.y=int(input("Enter the second Point"))

    def __str__(self):

        return "coordinates x and y is:"+str(self.x)+","+str(self.y)


p1=point2d()
p1.read_point()
print(p1)


class point3d(point2d):
    
    def read_3dpoint(self):
        self.z=int(input("Enter the third Point "))

    def __str__(self):

        return "coordinates x , y  and z are:"+str(self.x)+","+str(self.y)+","+str(self.z)
    def __init__(self):
        self.z=0

p2=point3d()
p2.read_3dpoint()
print(p2)
