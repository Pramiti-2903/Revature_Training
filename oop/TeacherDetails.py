from college import College

class TeacherDetail(College):
    def __init__(self, ccode, cname, empid, tname, dept):
        super().__init__(ccode, cname)
        self.empid=empid
        self.tname=tname
        self.dept=dept
    def display(self):
        print(f'{super()._ccode}\t {super()._cname}\n'
              f'{self.empid}\n {self.tname}\t{self.dept}')

