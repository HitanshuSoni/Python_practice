import threading
def print_cube(num):
    print("Cube:{}".format(num*num*num))
def print_sq(num):
    print("sq:{}".format(num*num))
if __name__=="__main__":
    
    t1=threading.Thread(target=print_sq,args=(10,))
    t2=threading.Thread(target=print_cube,args=(10,))
    t1.start()
    t1.join()
    t2.start()
    
    t2.join()
print("Done")
