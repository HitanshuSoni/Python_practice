class emploayee:
    '''def __init__():
        self.emp_id=0
        self.name=""
        self.basic_sal=0'''

    def readEmployee(self):
        self.emp_id=int(input("ENTER EMPLOYEE ID. "))
        self.name=str(input("ENTER NAME OF EMPLOYEE"))
        self.basic_sal=int(input("BASIC SALARY"))
        self.ta=float(input("ENTER THE T.A."))
        da=float(input("ENTER THE D.A."))
        hra=float(input("ENTER THE H.R.A."))
        tax=float(input("ENTER THE T.A.X."))

    def clacluation(self):
            ta=(ta*self.basic_sal)/100
            da=(da*self.basic_sal)/100
            hra=(hra*self.basic_sal)/100
            
            grossSal=self.basic_sal+ta+da+hra
            tax=(tax*grossSal)/100
            self.Netsal=grossSal-tax

    def __str__(self):
            return "Emp_id: "+str(self.emp_id)+"Emp. Name: "+self.name+"Basic Salary: "+str(self.basic_sal)+"Net Salary : "+str(self.Netsal)
E1=emploayee()
E1.readEmployee()
E1.clacluation()
print(E1)
        
        
        
