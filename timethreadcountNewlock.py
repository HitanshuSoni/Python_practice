import threading
import datetime

exitFlag=0
class myThread(threading.Thread):
        
	"""docstring for myThread"""
	def __init__(self,name,counter):
		threading.Thread.__init__(self)
		self.threadID=threadID
		self.name=name
		self.counter=counter
	def run(self):
		print("Starting"+self.name+"\n")
		#print_time(self.name,5,self.counter)
		#print("Exiting"+self.name+"\n")
		threadLock.acquire()
		self.print_date(self.name,self.counter)
		self.counter+=1
		threadLock.release()
		print("Exiting"+self.name+"\n")
    def print_date(self,threadName,counter):
    	datefields=[]
        today=datetime.date.today()
        datefields.append(today)
        print("%s[%d]:%s"%(threadName,counter,datefields[0]))
threadLock=threading.Lock()
treads=[]
thread1=myThread("Thread-1",1)
thread2=myThread("Thread-2",2)
thread1.start()
thread2.start()
threads.append(thread1)
threads.append(thread2)
for t in threads:
        t.join()
print("\nExit Main thread")			
		
		
		

