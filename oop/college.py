class College:
    def __init__(self,ccode,cname):
        self.ccode=ccode
        self.cname=cname
    def display(self):
        return self.ccode,self.cname