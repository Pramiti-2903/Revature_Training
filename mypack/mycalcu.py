from interest_calculations   import simple_interest
from shape_calculation import area_of_circle,area_of_square,area_of_rectangle
prin= float(input('principle :'))
ny=float(input('year :'))
roi=float(input('rate of interest :'))
length=float(input('enter the length of rectangle :'))
breadth=float(input('enter the breadth of rectangle :'))
print(f'Simple Interest :{simple_interest(prin=prin,ny=ny,roi=roi)[0]}'
      f'  Amount :{simple_interest(prin=prin,ny=ny,roi=roi)[1]}')
print(f'Area of circle :{area_of_circle(10)}'
      f'Area of rect :{area_of_rectangle(length, breadth)}')