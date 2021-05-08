import point2d
class point3d(point2d.point2d):
    
    def __init__(self):
        #super().__init__()
        point2d.point2d.__init__(self)
        self.z=0
        
    
    def read_3dpoint(self):
        point2d.point2d.read_point(self)
        self.z=int(input("Enter the third Point "))
        
        

    def __str__(self):

        return super().__str__()+" coordinates z is:"+str(self.z)
    

p2=point3d()
p2.read_3dpoint()
print(p2)
