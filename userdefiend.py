class Error(Exception):
    """Base class for other exception"""
    pass
class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass
class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass
number=10
while True:
    try:
        i_num=int(input("Enter a number:"))
        if i_num<number:
            raise ValueTooSmallError
        elif i_num>number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("Value too Small try again")
    except ValueTooLargeError:
        print("Value too Large try again")
print("you get corret Guesse")
        
