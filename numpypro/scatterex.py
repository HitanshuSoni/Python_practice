import matplotlib.pyplot as plt 
x=[1,2,3,4,5,6,7,8,9,10]
y=[2,4,5,7,6,8,9,11,12,12]
plt.scatter(x,y,label="starts",color="green",marker="*",s=50)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("My scatter plot")
plt.legend()
plt.show()