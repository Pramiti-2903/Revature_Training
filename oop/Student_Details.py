from college import College

class StudentDetails(College):
    def __init__(self, ccode, cname, roll_no, name, m1, m2, m3):
        super().__init__(ccode, cname)
        self.__roll_no = roll_no
        self.__name = name
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3

    def get_roll_no(self):
        return self.__roll_no

    def set_roll_no(self):
        return self.__roll_no

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def calc_tot(self):
        return self.__m1 + self.__m2 + self.__m3

    def calc_avg(self):
        return self.calc_tot() / 3
