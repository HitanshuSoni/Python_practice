class student:
    'Student'
    count=0
   

    def readStudent(self):
        self.name=str(input("ENTER THE NAME"))
        self.roll=int(input("ENTER THE ROLL NO."))
        n=int(input("ENTER THE NO. OF SUBJECTS "))
        self.marks=[]
        for i in range(0,n):
            
            marksli=int(input("Enter Marks: "))

            self.marks.append(marksli)
            student.count+=1
    def calculation(self):
        self.total=0
        '''self.maxmark=100
        self.totalmarks=self.n*self.maxmark'''

        #for self.item in self.marks:
        self.total=sum(self.marks)

        self.percent=self.total/len(self.marks)
        if self.percent<30:
            self.status="Fail"
        else:
            self.status="Pass"



    def __str__(self):

        return "Name:  "+self.name+"\nRoll_no.: "+str(self.roll)+"\npercent: "+str(self.percent)+"\nStatus: "+self.status+"Number of students: "+str(student.count)


S1=student()
S1.readStudent()
S1.calculation()
print(S1)
