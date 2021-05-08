a=int(input("Enter the Month to get Max. Day"))

if(a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12):
    print("Max. Days is 31")

elif(a==4 or a==6 or a==9 or a==11):
    print("Max. Days is 30")

else:
    print("It's Feb 28 or 29 Days")


