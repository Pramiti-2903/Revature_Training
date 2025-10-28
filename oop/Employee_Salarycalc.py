from oop.Employee import Employee

empid = int(input("Enter Employee ID: "))
ename = input("Enter Employee Name: ")
bp = float(input("Enter Basic Pay: "))

# Creating Employee object
employee = Employee(empid, ename, bp)

# Displaying results
print("\n------ Employee Salary Details ------")
print(f"Employee ID   : {employee.empid}")
print(f"Employee Name : {employee.ename}")
print(f"Gross Pay     : {employee.calc_grosspay():.2f}")
print(f"Net Pay       : {employee.calc_netpay():.2f}")