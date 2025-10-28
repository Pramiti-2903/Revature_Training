from  Student_Details import StudentDetails
class StudExCurr(StudentDetails):
    def __init__(self,ccode,cname,roll_no,name,m1,m2,m3,exm1,exm2):
        super().__init__(ccode,cname,roll_no,name,m1,m2,m3)

        self.exm1=exm1
        self.exm2=exm2
    def calc_extot(self):
        return self.exm1+self.exm2

