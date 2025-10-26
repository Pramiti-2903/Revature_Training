'''
date: 25/10/2025
Author:S.pramiti
Description:Program to find armstrong number
'''



num=int(input("enter a num: "))
num_str=str(num)
power=len(num_str)
arm=sum(int(r)**power for r in num_str)
if arm==num:
    print("It is a armstrong number")
else:
    print("It is not a armstrong number")


