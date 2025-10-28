from Student_extracurricular import StudExCurr
ccode=int(input('code: '))
cname=input('collage name: ')
roll_no=int(input("Enter your roll_no: "))
name=(input("Enter your name: "))
m1=int(input("Enter your m1: "))
m2=int(input("Enter your m2: "))
m3=int(input("Enter your m3: "))
exm1=int(input("Ex Mark 1: "))
exm2=int(input("Ex Mark 2: "))

stud = StudExCurr(ccode, cname, roll_no, name, m1, m2,m3, exm1, exm2)
print(f'{stud.display()[0]}\t {stud.display()[1]}\t')
print(f'{stud.get_roll_no()}\n{stud.name}\n'
      f'{stud.calc_tot()}\n'
      f'{stud.calc_avg()}\n')
print(f'{stud.calc_extot()}')