
from Arithcalculations import Arithcalculations
from AgenotenoughError import AgenotenoughError
num1=int(input("enter a num: "))
num2=int(input("enter another num: "))
age=int(input("enter age: "))
calc=Arithcalculations(num1,num2)

print(f'Addition: {calc.add()}')
print(f'subtraction: {calc.sub()}')
print(f'division: {calc.mul()}')
print(f'Multiplication: {calc.mul()}')
try:
    if num2==0:
        raise ZeroDivisionError("num2 is 0")
    if age<18:
        raise AgenotenoughError("your'e minor")
except ZeroDivisionError as zde:
    print(f'{zde}')
else:
 try:
    l1=[1,5,7,8]
    v1=l1[10]
    res=calc.div()
 except ZeroDivisionError:
    print("0 in dominator")
 except IndexError:
    print("index out of range")
 except:
    print("OOPS !")
 else:
    print("")

finally:
    print("Done")

