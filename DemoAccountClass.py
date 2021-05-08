class account:
    'account'
    
    def readaccount(self):
        self.name=str(input("ENTER THE NAME OF ACC. HOLDER"))
        self.account_no=int(input("ENTER THE ACCOUNT NO."))
        self.account_amt=float(input("ENTER THE AMT. IN ACCOUNT "))

    def withdis(self):
        chooice=int(input("press 1. for diposite \n press 2. for withdrwal\n"))
        if chooice==1:
            
            dip=float(input("Please Enter the Diposite Amt.\n"))
            if dip>25000:
                print("sorry you can't Diposite the Amt.\n")
            else:
                print("Congrasulations Amt. diposit\n" )
                self.amtdip=self.account_amt+dip
                print("Total Amt. after Diposite\n",self.amtdip)
        elif chooice==2:
            withdrwal=float(input("Please Enter the Diposite Amt.\n"))
            after_withd=self.account_amt-withdrwal
            if after_withd<1000:
                print("You Can't WithDrwal\n")
            else:
                print("Congrasulations Amt. WithDrwal\n")
                self.total_with=self.account_amt- withdrwal
                print("total Amt. after WirhDrawl\n",self.total_with)
    def __str__(self):
        return "NAME OF ACC. HOLDER \n"+self.name+"\n"+"ACCOUNT NO.\n"+str(self.account_no)+"\n"+"AMT. IN ACCOUNT \n"+str(self.account_amt)
            
            
a1=account()
a1.readaccount()
print(a1)
a1.withdis()
