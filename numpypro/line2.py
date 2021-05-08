import matplotlib.pyplot as plt 
x1=[1,2,3]
y1=[2,4,1]
plt.plot(x1,y1,label="line-1")
x2=[1,2,3]
y2=[4,1,3]
plt.plot(x2,y2,label="line-2")
plt.xlabel('x-lable')
plt.ylabel('y-lable')
plt.title("Two lines on same Graph")
plt.legend()
plt.show()