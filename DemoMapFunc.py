#map without lambda
def multiply(x):
    return x*2
print(list(map(multiply,[1,2,3,4])))


#map with lambda

print(list(map(lambda x:x*2,[1,2,3,4])))
