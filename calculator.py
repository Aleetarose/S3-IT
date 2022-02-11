"""************************************************************************************** 
ALEETA ROSE                           CALCULATOR
S3 IT
DATE:17/12/2021
ROLL NO:8
**************************************************************************************"""
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a , b):
    return a * b
def division(a , b):
    return a / b
def remainder(a , b):
	return a%b
def exponent(a , b):
	return a**b
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Division")
print("5.remainder")
print("6.exponent")
choice=input("please enter the choice(1/2/3/4/5/6):")
num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))


if choice=='1':
	print(num1,"+",num2,"=",add(num1,num2))
elif choice=='2':
	print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=='3':
	print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=='4':
	print(num1,"/",num2,"=",division(num1,num2))
elif choice=='5':
	print(num1,"%",num2,"=",remainder(num1,num2))
elif choice=='6':
	print(num1,"**",num2,"=",exponent(num1,num2))
else:
 print("invalid")
"""**********************************************************************

SAMPLE OUTPUT:

Select operation.
1.Add
2.Sub
3.Mul
4.Division
5.remainder
6.exponent
please enter the choice(1/2/3/4/5/6):4
enter the first number:55
enter the second number:2
55 / 2 = 27.5
**********************************************************************"""


