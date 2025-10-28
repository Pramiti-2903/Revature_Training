'''
date: 25/10/2025
Author:S.pramiti
Description:Program to calculate
'''

def calculate(m1,m2,m3):
    total=m1+m2+m3
    avg=total/3
    return total,avg
name=(input("Enter your name: "))
m1=int(input("Enter your mark1: "))
m2=int(input("Enter your mark2: "))
m3=int(input("Enter your mark3: "))

total,avg=calculate(m1, m2, m3)

print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", avg)