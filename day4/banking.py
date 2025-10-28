from mypack.interest_calculations import simple_interest,compound_interest

prin= float(input('principle :'))
ny=float(input('year :'))
roi=float(input('rate of interest :'))

si,amt=simple_interest(prin=prin,ny=ny,roi=roi)
print(f'SI : {si} Amount : {amt}')

amount=compound_interest(prin=prin,t=t,roi=roi)
print(f' Amount : {amount}')