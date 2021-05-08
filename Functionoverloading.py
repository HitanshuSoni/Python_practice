'''def f(n):
    return n+42
def f(n,m):
    return n+m+42
f(3,4)
f(3)'''

def f(n,m=None):
    if m:
        return n+m+42
    else:
        return n+42
print(f(3,4))
print(f(5))

def g(*x):
    if len(x)==1:
        return x[0]+42
    else:
        return x[0]+x[1]+42
print(g(4))

