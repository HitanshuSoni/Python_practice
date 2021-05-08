import time
from threading import Thread
import threading

def sleepMe(i):
    print("Thread %s going to sleep for 5 seconds.\n"%threading.current_thread())
    time.sleep(5)
    print("Thread %s is awake now .\n"%threading.current_thread())

for i in range(5):
    th=Thread(target=sleepMe,args=(i,))
    th.start()
#print("Current Thread Count:%i.\n"%threading.active_count())
