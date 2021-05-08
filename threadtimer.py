import threading
def delayed():
    print("I am printing after 5 seconds\n ")
th=threading.Timer(5,delayed)
th.start()
