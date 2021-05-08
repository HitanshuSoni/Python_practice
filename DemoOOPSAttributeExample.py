class Robot(object):
    pass
    

x=Robot()
Robot.brand="Hitu"
print(x.brand)
x.brand="Shivuu"
print(Robot.brand)
y=Robot()
print(y.brand)
Robot.brand="Soni"
print(y.brand)
print(x.brand)
print(x.__dict__)
print(y.__dict__)
print(Robot.__dict__)


