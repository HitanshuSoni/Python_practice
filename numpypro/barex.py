import matplotlib.pyplot as plt
left=[1,2,3,4,5]
height=[10,24,36,40,5]
tick=['one','two','three','four','five']
plt.bar(left,height,tick_label=tick,width=0.8,color=['red','green'])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("My Bar Chart!")
plt.show()