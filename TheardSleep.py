import time
from threading import Thread
import threading

def sleepMe(i):
    print("Thread %i going to sleep for 5 seconds.\n"%i)
    time.sleep(5)
    print("Thread %i is awake now .\n"%i)

for i in range(5):
    th=Thread(target=sleepMe,args=(i,))
    th.start()
print("Current Thread Count:%i.\n"%threading.active_count())
