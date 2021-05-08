class Robot:
    pass
x=Robot()
y=Robot()
x.name="Marvin"
x.build_year="1973"
y.name="Caliban"
y.build_year="1999"
print(x.name)
print(y.build_year)
print(x.__dict__)
print(y.__dict__)
