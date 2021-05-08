nestLam=lambda x,fun:x+fun(x)
print(nestLam(2,lambda x:3+x))
