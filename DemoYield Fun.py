def checkyield():
    yield 1
    yield 2
    yield 3
    '''return 1
    return 2'''
for value in checkyield():
    print(value)
