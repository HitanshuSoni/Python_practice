import time
import threading
import logging
logging.basicConfig(level=logging.DEBUG,format="[%(levelname)s](%(thredName)-10s) %(message)s",)
def worker():
	logging.debug("Satrting")
	time.sleep(2)
	logging.debug("Exiting")
def my_service():
	logging.debug("Satrting")
	time.sleep(3)
	logging.debug("Exiting")

t=threading.Thread(name="my_service",target=my_service)
w=threading.Thread(name="worker",target=worker)
w2=threading.Thread(target=worker)
w.start()
w2.start()
t.start()
	
